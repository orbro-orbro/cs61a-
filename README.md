# CS61A 自学仓库

这是我跟学 UC Berkeley **CS61A: Structure and Interpretation of Computer Programs** 的代码仓库。课程前半段用 Python 讲编程基础与函数式思想，后半段用 Scheme 讲解释器——抽象力拉满。这里放作业、Project 和学习笔记，持续更新。

## 目录结构

```
cs61a/
├── hw01/          # 作业：函数、控制流
├── hw02/          # 作业：高阶函数、accumulate 抽象
├── hog/           # Project 1: The Game of Hog（骰子游戏）
├── note/          # 学习笔记
└── README.md
```

## 作业

| 目录 | 文件 | 做了什么 |
|------|------|----------|
| `hw01/` | `hw01.py` | `a_plus_abs_b`（不用 `abs` 实现 a+\|b\|）、`two_of_three`（三数取两小，求平方和）、`largest_factor`（找最大真因数）、`hailstone`（冰雹序列 / Collatz 猜想） |
| `hw02/` | `hw02.py` | `product`（连乘）、`accumulate`（通用 fuse 抽象——加和乘只是它的特例）、`summation_using_accumulate` / `product_using_accumulate`（用 accumulate 一行实现求和/求积）、`make_repeater`（返回复合 n 次 f 的函数，闭包初体验） |

每一题都有 doctest，写完直接跑验证，很有 TDD 的感觉。

## 笔记

| 文件 | 内容 |
|------|------|
| `note/main.py` | 短路求值（`and`/`or` 的求值策略）、自制 `if_` 函数 |
| `note/higher order function.py` | 高阶函数：`summation` 通项求和、`make_adder` 闭包造函数、`assert` 断言用法 |

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

---

> 持续更新中，和 CS61A 一起变强 💪
