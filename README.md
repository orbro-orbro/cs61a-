# CS61A 自学仓库

这是我跟学 UC Berkeley **CS61A: Structure and Interpretation of Computer Programs** 的代码仓库。课程前半段用 Python 讲编程基础与函数式思想，后半段用 Scheme 讲解释器——抽象力拉满。这里放作业、Project 和学习笔记，持续更新。

## 目录结构

```
cs61a/
├── hw01/          # 作业：函数、控制流
├── hw02/          # 作业：高阶函数、accumulate 抽象
├── hw03/          # 作业：递归
├── lab03/         # Lab：列表操作与递归
├── lab04/         # Lab：高阶函数与数据抽象（树）
├── hog/           # Project 1: The Game of Hog（骰子游戏）
├── cats/          # Project 2: Cats（打字测试与自动纠错）
├── note/          # 学习笔记
└── README.md
```

## 作业

| 目录 | 文件 | 做了什么 |
|------|------|----------|
| `hw01/` | `hw01.py` | `a_plus_abs_b`（不用 `abs` 实现 a+\|b\|）、`two_of_three`（三数取两小，求平方和）、`largest_factor`（找最大真因数）、`hailstone`（冰雹序列 / Collatz 猜想） |
| `hw02/` | `hw02.py` | `product`（连乘）、`accumulate`（通用 fuse 抽象——加和乘只是它的特例）、`summation_using_accumulate` / `product_using_accumulate`（用 accumulate 一行实现求和/求积）、`make_repeater`（返回复合 n 次 f 的函数，闭包初体验） |
| `hw03/` | `hw02.py` | `num_eights`（数位上 8 的个数）、`digit_distance`（相邻数位差的绝对值之和）、`interleaved_sum`（奇偶位交替求和，从 1 递推 n）、`next_smaller_dollar` / `next_larger_dollar`（找各位递减/递增的美元金额）、`count_dollars`（递归计数到目标金额）、`shuffle`（交错合并列表两半）、`deep_map`（递归映射嵌套列表） |

## Lab

| 目录 | 文件 | 做了什么 |
|------|------|----------|
| `lab03/` | `lab03.py` | `flatten`（展平嵌套列表）、`close_list`（找最近的 k 个相邻元素）、`remove_first`（按值删除首个匹配项）、`sort`（选择排序）、`make_onion`（函数洋葱：`f(g(x))` → `g(f(x))`）、`make_func_repeater`（把函数重复应用 n 次）、`ten_pairs`（统计和为 10 的数位对）、`count_digit`（统计数字 n 中某数位的出现次数） |
| `lab04/` | `lab04.py` | 自实现 `my_map` / `my_filter` / `my_reduce`，城市数据抽象（`make_city` / `get_name` / `get_lat` / `get_lon` → `distance` / `closer_city`），树抽象（`sum_tree` 递归求和、`balanced` 判断分支数是否递减、`num_trees` 枚举所有树形、`only_paths` 从标签构造路径树） |

每一题都有 doctest，写完直接跑验证，很有 TDD 的感觉。

## 笔记

| 文件 | 内容 |
|------|------|
| `note/main.py` | 短路求值（`and`/`or` 的求值策略）、自制 `if_` 函数 |
| `note/higher order function.py` | 高阶函数：`summation` 通项求和、`make_adder` 闭包造函数、`assert` 断言用法 |
| `note/recursion.py` | 递归入门：`sum_digit`（数位求和）、`fact`（阶乘） |
| `note/Functional Abstraction.py` | 作用域与闭包：`search` 暴力搜索构造反函数、`trace` 装饰器、`horse/mask` 命名混淆与帧分析 |
| `note/treerecursion.py` | 树递归全攻略：`cascade` 级联打印、`f_then_g` 高阶递归骨架（grow/shrink/inverse）、Fib、Counting Partitions，附 lambda 详解 |
| `note/Sequence and Containers.py` | 序列与容器：List/Range/String/Dict 全覆盖，切片、列表推导式、序列聚合（sum/max/min）、解包与成员检测 |
| `note/Mutability and Data Abstraction.py` | 数据抽象：构造器与选择器的分离思想，以有理数（rational）为例用闭包实现 ADT |
| `note/Tree.py` | 树 ADT（嵌套列表表示）：`fib_tree` 斐波那契树、`print_sums` 路径和、`count_leaves` / `count_paths` 等递归操作 |

## Project: The Game of Hog 🐗

Hog 是一个骰子游戏模拟器与策略系统，两个玩家轮流掷骰子，先到 100 分者获胜。

### 三条奇葩规则

- **Sow Sad**：掷出任何一个 1，本回合得分直接变成 1（手气不好别哭）
- **Boar Brawl**：选择掷 0 个骰子时，得分由对手分数的十位数和自己分数的个位数决定——拼的不是运气，是数学
- **Sus Fuss**：新总分如果恰好有 3 或 4 个因数，直接跳到下一个素数（"你的分数很可疑，换个素数吧"）

### 项目亮点

代码采用 **策略与规则分离** 的设计：策略函数只管"掷几个骰子"，规则由 update 函数统一执行。换个规则集只需传入不同的 update 函数，策略代码一行不用改。骰子也被抽象成一个零参数函数，方便用确定性骰子做测试。

项目实现了从 `always_roll_5`（无脑掷 5）到 `final_strategy`（动态遍历 1-10 个骰子选最优）的多层策略，可以 AI vs AI 观战，也可以真人对战。

### 运行方式

```bash
cd hog
python hog_gui.py              # 图形界面
python hog_ui.py -n 0          # AI vs AI 观战
python hog_ui.py -n 1          # 真人 vs AI
python hog.py -r               # 策略胜率实验
如果无法执行，可以考虑将python换成py，或者python3
```

## Project: Cats 🐱

Cats（Computer Aided Typing Software）是一个打字测试与自动纠错系统。用户在命令行里按主题选段落、限时打字，程序实时统计速度和准确率；背后还实现了一套编辑距离算法驱动的拼写纠错引擎，以及多人打字比赛的数据统计模块。

### 四个阶段

- **Phase 1 — Typing**：段落筛选（`pick` + `about`）、准确率（`accuracy`）和 WPM 速度（`wpm`）计算——把打字测试跑起来的基础。
- **Phase 2 — Autocorrect**：自动纠错核心。`autocorrect` 用差异函数从词表中找最佳匹配；`furry_fixes` 只允许替换字符；`minimum_mewtations` 是完整编辑距离（插入/删除/替换），带 `limit` 剪枝。可选扩展 `final_diff` 还加入了相邻字符交换（Damerau 步），让纠错更聪明。
- **Phase 3 — Multiplayer**：`report_progress` 上传进度、`time_per_word` 将时间戳转为逐词耗时、`fastest_words` 按单词判最快玩家——一个简易的多人对战统计系统。
- **Phase 4 (EC)** — Efficiency：实现 `memo_diff` 带缓存装饰器，避免同一对单词在不同 `limit` 下重复递归。缓存键是 `(entered, source)` 对，新 `limit` 小于等于缓存 `limit` 时直接复用，否则重新计算并更新。

### 项目亮点

**编辑距离 + 剪枝**是 Cats 最有算法味的部分。`furry_fixes` → `minimum_mewtations` → `final_diff` 层层递进，从只允许替换到允许增删改再到交换相邻字符。`limit` 参数贯穿所有 diff 函数，一旦当前差异超过上限立即剪枝返回，避免穷举——这是递归搜索中剪枝策略的典型应用。

**多玩家数据处理**：`time_per_word` 把每个玩家的累计时间戳转为逐词耗时，`fastest_words` 再按单词判胜负——本质上是一个按列求 argmin 再按玩家分组的操作，练习了二维列表的遍历和字典组装。

**memo_diff 的缓存策略**与普通 memoization 不同：新 `limit` 比旧 `limit` 更宽松时需要重新计算（因为更大的 `limit` 可能找到更优解），否则直接复用缓存。这是一个"带阈值的记忆化"，比无脑 memo 多了一层判断逻辑。

### 运行方式

```bash
cd cats
python cats.py -t              # 无主题，随机段落
python cats.py -t dog          # 只练习包含 dog 的段落
python cats_gui.py             # 图形界面（多人模式）
python ok                      # 课程自带测试
如果无法执行，可以考虑将python换成py，或者python3
```

---

> 持续更新中，和 CS61A 一起变强 💪
