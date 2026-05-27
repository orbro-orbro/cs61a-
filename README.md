# CS61A 自学仓库 🎲

这是我跟学 UC Berkeley **CS61A: Structure and Interpretation of Computer Programs** 的代码仓库，包含课程作业和项目。

## 目录结构

```
cs61a/
├── hw01/          # 作业：变量、控制流、基础函数
├── hog/           # Project 1: The Game of Hog
├── note/          # 学习笔记（高阶函数等）
└── README.md
```

## 作业

| 目录 | 内容 |
|------|------|
| `hw01/` | 入门练习，涵盖变量绑定、条件判断、循环和基础函数定义 |

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
