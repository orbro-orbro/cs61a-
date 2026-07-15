# Cats: Computer Aided Typing Software

这是一个基于 CS 61A "Cats" 项目的打字测试程序。项目的核心目标是练习英文打字速度与准确率，并实现一组与自动纠错、编辑距离和多人打字统计相关的函数。

## 项目内容

- `cats.py`：主程序和所有核心函数的实现位置。
- `cats_gui.py`：图形界面入口。
- `cats.ok` / `ok`：课程提供的自动测试工具。
- `data/`：打字测试所用的文本数据。
- `tests/`：本项目相关测试文件。
- `multiplayer/`：多人打字比赛相关模块。
- `cats_函数说明.md`：中文函数说明文档。

## 主要功能

项目中会涉及下面这些能力：

- 按主题筛选段落并进行打字练习。
- 计算输入内容的准确率 `accuracy`。
- 计算打字速度 `wpm`。
- 实现自动纠错 `autocorrect`。
- 计算字符串差异函数，如 `furry_fixes`、`minimum_mewtations` 和 `final_diff`。
- 支持多人进度汇报与统计。

## 如何运行

在项目根目录下打开 PowerShell，然后执行：

```powershell
cd C:\Users\lenovo\Desktop\cs61a\cats
& C:/Users/lenovo/AppData/Local/Programs/Python/Python39/python.exe cats.py -t
```

如果想带主题词练习，例如 `dog`，可以执行：

```powershell
& C:/Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe cats.py -t dog
```

## 如何测试

如果你想运行课程自带的测试，可以使用 `ok`：

```powershell
& C:/Users/lenovo/AppData/Local/Programs/Python/Python39/python.exe ok
```

也可以只检查语法：

```powershell
& C:/Users/lenovo/AppData/Local/Programs/Python/Python39/python.exe -m py_compile cats.py
```

## 说明

- 本项目是课程作业风格的练习项目，重点在于函数实现和算法理解。
- 如果你修改了 `cats.py`，建议先跑一次语法检查，再运行 `ok` 进行验证。
- `cats_gui.py` 可用于图形界面体验，但命令行模式通常更适合调试和测试。
