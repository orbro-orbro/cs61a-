# CS 61A Cats 项目函数说明

本文档整理的是 Cats 项目中需要学生在 `cats.py` 里独立完成的函数，包括函数名、参数和核心功能。

## Phase 1: Typing

| 函数名 | 参数 | 功能 |
| --- | --- | --- |
| `pick` | `paragraphs: list[str]`, `select: function`, `k: int` | 从 `paragraphs` 中筛选出满足 `select` 条件的段落，返回第 `k` 个符合条件的段落；如果数量不够，返回空字符串。 |
| `about` | `keywords: list[str]` | 返回一个选择函数；该函数判断某个段落是否包含 `keywords` 中任意一个单词。比较时忽略大小写和标点，并且必须是完整单词匹配，不能只匹配子串。 |
| `accuracy` | `entered: str`, `source: str` | 计算 `entered` 与 `source` 对应位置单词的匹配准确率，返回百分比。要求按单词位置一一比较，大小写和标点都算作不同。 |
| `wpm` | `entered: str`, `elapsed: int` | 计算输入字符串的 words per minute（WPM）。公式是：字符数除以 5，再除以耗时分钟数。 |

### 详细要求

#### `pick`

- `k` 是非负整数。
- 从 `paragraphs` 中只统计那些让 `select(paragraph)` 返回 `True` 的段落。
- 返回第 `k` 个符合条件的段落，索引从 0 开始。
- 如果符合条件的段落数量不足 `k + 1`，返回空字符串。

#### `about`

- `keywords` 必须全部是小写；题目模板里会用断言检查这一点。
- 先对段落去掉标点，再转成小写，再按空格切分成单词列表。
- 只做完整单词匹配，不做子串匹配。
- 只要段落中出现 `keywords` 里的任意一个单词，就返回 `True`，否则返回 `False`。

#### `accuracy`

- 按空白字符分隔单词进行比较。
- 只比较 `entered` 中已有的单词，和 `source` 中对应位置的单词。
- 每个位置必须完全一致，大小写和标点都必须相同。
- 如果 `entered` 比 `source` 长，超出的单词全部算错。
- 如果 `entered` 比 `source` 短，而且目前为止都匹配，则准确率是 `100.0`。
- 如果 `entered` 和 `source` 都为空，准确率是 `100.0`。
- 如果 `entered` 为空而 `source` 非空，准确率是 `0.0`。
- 如果 `entered` 非空而 `source` 为空，准确率是 `0.0`。

#### `wpm`

- `elapsed` 必须大于 0，题目模板会断言这一点。
- 字符数包括空格在内的全部字符。
- 公式是：`len(entered) / 5 / (elapsed / 60)`。

## Phase 2: Autocorrect

| 函数名 | 参数 | 功能 |
| --- | --- | --- |
| `autocorrect` | `entered_word: str`, `word_list: list[str]`, `diff_function: function`, `limit: int` | 若 `entered_word` 已在 `word_list` 中，直接返回它；否则找出与它差异最小的候选词。若最小差异大于 `limit`，返回原词。若并列，返回在 `word_list` 中更靠前的词。 |
| `furry_fixes` | `entered: str`, `source: str`, `limit: int` | 一个递归差异函数：计算将 `entered` 通过替换字符变成 `source` 所需的最少替换次数，再加上长度差；当差异已经超过 `limit` 时可提前停止。 |
| `minimum_mewtations` | `entered: str`, `source: str`, `limit: int` | 计算把 `entered` 变成 `source` 的最少编辑次数，允许的操作是插入、删除、替换；同样要使用 `limit` 提前剪枝，减少不必要的递归。 |

### 详细要求

#### `autocorrect`

- `entered_word` 已经假定是小写且没有标点。
- 如果 `entered_word` 本身就在 `word_list` 中，直接返回它。
- 否则比较 `entered_word` 和 `word_list` 里每个词的差异。
- 返回差异最小的那个词。
- 如果最小差异大于 `limit`，返回 `entered_word`。
- 如果有多个词并列最小，返回在 `word_list` 中最靠前的那个。
- `diff_function` 接收三个参数：`entered_word`、`source_word`、`limit`。

#### `furry_fixes`

- 这是一个递归 diff 函数。
- 计算把 `entered` 变成 `source` 需要替换多少个字符，再加上长度差。
- 如果字符串长度不同，长度差直接计入最终差异。
- 不能使用 `while`、`for` 或列表推导式。
- 如果差异已经大于 `limit`，可以提前停止递归并返回任意大于 `limit` 的值。

#### `minimum_mewtations`

- 这是一个更高级的递归 diff 函数。
- 允许三种编辑操作：插入、删除、替换。
- 题目要求在 `limit` 被超过时尽早停止递归。
- 不能再额外写 helper 函数，否则自动评分可能失败。
- 模板里给了 `assert False, 'Remove this line'`，正式实现时必须删除它。

### 可选扩展

| 函数名 | 参数 | 功能 |
| --- | --- | --- |
| `final_diff` | `entered: str`, `source: str`, `limit: int` | 自定义差异函数，可用于让 autocorrect 更智能。该函数是可选扩展，不影响基础得分。 |

### 详细要求

- `final_diff` 是可选题，不影响必做题得分。
- 可以设计更聪明的差异规则，例如考虑邻近键位、重复字母、交换相邻字母等。
- `FINAL_DIFF_LIMIT` 可以在 `cats.py` 里按需要调整。

## Phase 4: Efficiency（可选加分）

| 函数名 | 参数 | 功能 |
| --- | --- | --- |
| `memo_diff` | `diff_function: function` | 返回一个带缓存的差异函数；对于同一对 `entered` 和 `source`，如果新传入的 `limit` 不大于已缓存的限制，就直接复用缓存结果，否则重新计算并更新缓存。 |

## 说明

Phase 4 里提供的 `memo` 是框架函数，不需要学生自己实现；真正需要完成的是 `memo_diff`，以及在项目后续按要求把它用于相关函数装饰。

### 详细要求

#### `memo_diff`

- 它接收一个 `diff_function`，并返回一个新的 diff 函数 `memoized`。
- 缓存的键是 `(entered, source)` 这一对字符串。
- 缓存中还要记录上一次使用的 `limit`。
- 如果同一对 `(entered, source)` 再次出现，并且新传入的 `limit` 小于等于已缓存的 `limit`，直接返回缓存值。
- 如果新 `limit` 更大，就重新计算并更新缓存。
- 缓存里的数据要使用元组而不是列表。

## Phase 3: Multiplayer

| 函数名 | 参数 | 功能 |
| --- | --- | --- |
| `report_progress` | `entered`, `source`, `user_id`, `upload` | 计算当前已正确输入的前缀进度，并通过 `upload` 上传一个包含 `id` 和 `progress` 的字典，同时返回进度值。 |
| `time_per_word` | `words`, `timestamps_per_player` | 把每个玩家的累计时间戳转换成逐词耗时，返回一个字典，包含原始 `words` 和对应的 `times`。 |
| `fastest_words` | `words_and_times` | 根据每个玩家的逐词耗时，找出每个单词是谁打得最快，并按玩家分组返回结果；平局时索引更小的玩家获胜，且不能修改输入数据。 |

### 详细要求

#### `report_progress`

- 每次用户完成一个单词时调用。
- `entered` 是到目前为止用户已经输入的单词列表。
- `source` 是目标文本的单词列表。
- 进度定义为：从开头起连续正确输入的单词数，除以 `source` 的总单词数。
- 一旦遇到第一个错误单词，就停止继续比较。
- 必须调用 `upload` 上传一个字典，字典包含两个键：`'id'` 和 `'progress'`。
- `'id'` 对应 `user_id`，`'progress'` 对应计算出的进度。
- 返回这个进度值。

#### `time_per_word`

- `words` 是玩家要打的单词列表。
- `timestamps_per_player` 是二维列表，每个内层列表表示一个玩家的累计时间戳。
- 每个内层列表的第一个时间戳表示开始输入的时间。
- 返回结果是一个字典，结构必须是 `{'words': words, 'times': times}`。
- `times[i][j]` 表示第 `i` 个玩家打第 `j` 个单词所用的时间。
- 这个时间是相邻累计时间戳的差值。

#### `fastest_words`

- 输入是 `time_per_word` 返回的字典。
- 返回值是一个列表，里面每个元素也是一个列表，对应一个玩家。
- 对于每个单词，找出用时最短的玩家，把这个单词分配给该玩家。
- 如果出现平局，索引更小的玩家算最快。
- 不能修改输入的玩家时间列表。
- 要能处理任意数量的玩家，不只两个。

## 备注

- 这个项目实际需要修改的核心文件是 `cats.py`。
- 题目中已经给出的辅助函数和框架函数不需要学生自己实现。
- `minimum_mewtations` 在模板里带有 `count(...)` 包装，这是作业要求的一部分，不能删掉。