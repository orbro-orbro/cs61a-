# The Game of Hog

CS 61A Hog 项目 —— 一个骰子游戏的模拟器与策略系统。

## 游戏规则

两名玩家轮流行动，每回合选择掷 **0 到 10 个六面骰子**，先达到 100 分者获胜。

三条核心规则：

| 规则 | 触发条件 | 效果 |
|---|---|---|
| **Sow Sad** | 掷出任意一个 1 | 本回合得分变为 1 |
| **Boar Brawl** | 选择掷 0 个骰子 | 得分 = max(3 × |对手十位数 − 自己个位数|, 1) |
| **Sus Fuss** | 新总分有恰好 3 或 4 个因数 | 总分跳到下一个素数 |

## 项目结构

```
hog.py          # 核心逻辑（我实现的部分）
hog_ui.py       # 命令行界面（真人 vs AI）
hog_gui.py      # 图形界面
dice.py         # 骰子系统（公平骰子 / 测试骰子）
ucb.py          # 课程工具库
```

## 函数调用链

从底层到顶层，整个项目的逻辑分为四层：

### 第一层：基础得分规则

**`roll_dice(num_rolls, dice)`** — 掷骰子并应用 Sow Sad 规则。
掷 num_rolls 次，出现任何一个 1 就返回 1，否则返回总和。

**`boar_brawl(player_score, opponent_score)`** — 掷 0 个骰子时的得分计算。
取对手分数的十位数和自己分数的个位数，返回 3×|差值| 和 1 的较大值。

### 第二层：一回合得分

**`take_turn(num_rolls, player_score, opponent_score, dice)`**
根据 num_rolls 选择路径，返回本回合获得的分数（增量）：
- num_rolls > 0 → 调用 `roll_dice`
- num_rolls = 0 → 调用 `boar_brawl`

### 第三层：更新总分

**`simple_update(...)`** — 简单版更新：旧分 + 本回合得分 → 新总分。仅含 Sow Sad 和 Boar Brawl。

**`sus_update(...)`** — 完整版更新：先和 simple_update 一样计算，再对结果应用 Sus Fuss 规则。

辅助函数：
- **`is_prime(n)`** — 判断 n 是否为素数
- **`num_factors(n)`** — 返回 n 的因数个数（含 1 和 n）
- **`sus_points(score)`** — 若分数有 3 或 4 个因数，则跳到下一个素数；否则不变

### 第四层：一局游戏

**`play(strategy0, strategy1, update, ...)`**
主循环：双方轮流，每回合用策略函数决定掷几个骰子，用 update 函数更新分数，直到一方达到目标分数。

`play` 通过传入不同的 `update` 来控制规则集：
- `play(..., simple_update)` → 仅 Sow Sad + Boar Brawl
- `play(..., sus_update)` → 全部三条规则

### 第五层：策略系统

策略函数接收（自己分数, 对手分数），返回掷几个骰子：

| 策略 | 逻辑 |
|---|---|
| `always_roll_5` | 永远掷 5 个 |
| `catch_up` | 落后掷 6，持平或领先掷 5 |
| `always_roll(n)` | 返回一个永远掷 n 个的策略 |
| `boar_strategy` | Boar Brawl 收益 ≥ 阈值时掷 0，否则掷 N |
| `sus_strategy` | 考虑 Sus Fuss 后掷 0 收益 ≥ 阈值时掷 0，否则掷 N |
| `final_strategy` | 动态最优：遍历 1-10 个骰子，挑期望增量最大的作为阈值，掷 0 达标则用 Boar Brawl |

评估工具：
- **`winner(s0, s1)`** — 两个策略对战一局，返回赢家
- **`average_win_rate(s, baseline)`** — 计算策略对基准策略的胜率（模拟 1000 局）
- **`max_scoring_num_rolls(dice)`** — 找出单回合平均得分最高的掷骰子数

## 完整调用链

```
play(strategy, strategy, sus_update)
  │
  ├── strategy(score, opponent_score)       → 决定掷几个骰子
  │
  └── sus_update(num_rolls, score, opp, dice)
        │
        ├── take_turn(num_rolls, score, opp, dice)
        │     ├── roll_dice(num_rolls, dice)      [掷骰子 → Sow Sad]
        │     └── boar_brawl(score, opp)           [掷零个 → Boar Brawl]
        │
        └── sus_points(score + 本回合得分)
              ├── num_factors(score)              [统计因数]
              └── is_prime(n)                     [找下一个素数]
```

## 运行方式

```bash
# Web 图形界面 → 浏览器打开 http://localhost:31415
python hog_gui.py

# 命令行界面
python hog_ui.py -n 0   # AI vs AI 观战
python hog_ui.py -n 1   # 真人 vs AI
python hog_ui.py -n 2   # 两人对战

# 运行策略实验（比较各策略胜率）
python hog.py -r
```

## 关键设计思想

**策略与规则分离**：策略函数只决定掷几个骰子，规则由 update 函数统一执行。给 play 传不同的 update 就能切换规则集，策略代码完全不用改。

**骰子抽象**：骰子是一个零参数函数 `dice()`，每次调用返回一个值。`make_test_dice(1, 2, 3)` 返回一个循环 1→2→3→1... 的确定性骰子，方便测试。
