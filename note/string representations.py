# =============================================================================
# CS61A 字符串表示笔记
# =============================================================================

# =============================================================================
# 一、F-Strings（格式化字符串）
# =============================================================================

# f-string 是 Python 推荐的字符串插值方式。在引号前加 f，花括号内嵌表达式。
# 计算时，每个 {} 里的表达式会被 str() 转换后插入字符串。

name = "orbro"
score = 95
print(f"{name} scored {score}")          # orbro scored 95
print(f"{name} scored {score + 5}")      # orbro scored 100  (表达式也行)
print(f"pi starts with {3.14159}...")    # pi starts with 3.14159...

# 与旧式写法的对比：
# "{} scored {}".format(name, score)   -- .format() 方式（旧）
# name + " scored " + str(score)       -- 手动拼接（繁琐）
# f-string 最简洁，且性能最好。

# =============================================================================
# 二、两个字符串表示：__str__ vs __repr__
# =============================================================================

# Python 规定：每个对象都应该提供两种字符串表示。
#
#   str() / __str__  : 给人看的，可读性优先（informal）
#   repr() / __repr__: 给开发者/调试看的，无歧义优先
#                     理想情况下 eval(repr(x)) 能重建对象
#
# 一句话：str 给用户看，repr 给 Python 看。

# --- 默认行为 ---
# 如果类没有定义 __str__，调用 str() 时会回退到 __repr__。
# 如果两个都没定义，继承自 object 的默认 __repr__ 返回：
#   <模块名.类名 object at 0x内存地址>

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("旺财")
print(str(d))   # <__main__.Dog object at 0x...>  (默认，啥也看不出来)
print(repr(d))  # <__main__.Dog object at 0x...>  (同上)

# --- 手动实现 ---

class Rational:
    """有理数：分子/分母，自动约分"""

    def __init__(self, numer, denom):
        from math import gcd
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __str__(self):
        """给人看：像分数的样子"""
        return f"{self.numer}/{self.denom}"

    def __repr__(self):
        """给 Python 看：能直接 eval 还原的表达式"""
        return f"Rational({self.numer}, {self.denom})"

half = Rational(1, 2)
print(half)       # 1/2                    (调用 __str__)
print(str(half))  # 1/2                    (同上)
print(repr(half)) # Rational(1, 2)         (调用 __repr__)
half              # Rational(1, 2)         (交互式环境默认用 repr)

# =============================================================================
# 三、eval 与 repr 的关系
# =============================================================================

# eval() 把字符串当作 Python 表达式执行，返回结果。
# repr() 设计目标：输出一个字符串，这个字符串传给 eval 能重建原对象。

from fractions import Fraction
f = Fraction(1, 3)
f2 = eval(repr(f))     # repr 输出 "Fraction(1, 3)"，eval 执行它
print(f2)              # 1/3
print(type(f2))        # <class 'fractions.Fraction'>
print(f == f2)         # True  (值相等)

# 但这不是数学上的"互逆"：
#   eval(repr(3))  = 3   ✅ 这个方向"大致"成立
#   eval(repr(obj)) 对自定义类，只有写了正确的 __repr__ 才行
#
#   repr(eval("3"))   = "3"
#   repr(eval("1+2")) = "3"   同一个结果，不同字符串
#   repr(eval(s)) ≈ s  ❌ 这个方向完全不成立
#
# 此外：eval 只能处理表达式，不能执行语句（if/for/赋值等）
# ⚠️  永远不要 eval 用户输入！它是任意代码执行，严重安全漏洞。

# =============================================================================
# 四、容器中的 repr 行为
# =============================================================================

# 容器（list, dict, tuple）内部元素永远用 repr，即使外层调的是 str。

class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"🐱 {self.name}"
    def __repr__(self):
        return f"Cat('{self.name}')"

c = Cat("咪咪")
print(c)         # 🐱 咪咪           (str)
print([c])       # [Cat('咪咪')]     (list 内部用 repr！)
print(str([c]))  # [Cat('咪咪')]     同上
print(f"{c}")    # 🐱 咪咪           (f-string 调用 str)

# =============================================================================
# 五、调用链路总结
# =============================================================================

# print(x)  →  str(x)  →  type(x).__str__(x)
#                              ↓ 若不存在
#                           type(x).__repr__(x)
#
# repr(x)   →  type(x).__repr__(x)    (不走 __str__，无回退)
#
# 交互式环境显示值  →  repr(x)

# =============================================================================
# 六、其他常见双下划线方法（Dunder Methods）
# =============================================================================

# __init__   构造对象                 Obj(...)
# __str__    给人看的字符串           str(x), print(x)
# __repr__   给 Python 看的字符串     repr(x), 交互式显示
# __add__    加法                    x + y
# __radd__   反向加法                y + x (当 y 的 __add__ 不认识 x 时)
# __mul__    乘法                    x * y
# __bool__   真值判断                if x: / bool(x)
# __float__  转浮点数                float(x)
# __len__    长度                    len(x)
# __getitem__ 索引/切片              x[i] / x[i:j]
# __call__   把实例当函数调用         x()
# __eq__     相等比较                x == y
# __lt__     小于比较                x < y
# __iter__   返回迭代器              for e in x:
# __next__   迭代器的下一个值         next(it)

# 这些方法构成 Python 的"协议"——你实现了对应方法，你的类就能用对应语法。
# 这就是鸭子类型：不管你是谁，有 __len__ 就能 len()，有 __getitem__ 就能 []

# =============================================================================
# 七、多态与接口
# =============================================================================

# 接口（Interface）：一组共享的方法名和行为约定。
# __str__ 和 __repr__ 本身就是接口——任何类实现它们后，
# str() 和 repr() 就能以多态的方式工作，无需知道对象的具体类型。

# 多态的好处：同一个函数可以操作任意类型的对象，只要它们有相同的接口。

def show(obj):
    """对任意对象打印两种表示"""
    print(f"str  : {str(obj)}")
    print(f"repr : {repr(obj)}")

show(Rational(1, 3))   # 对 Rational 有效
show(Cat("旺财"))       # 对 Cat 也有效
show([1, 2, 3])        # 对 list 同样有效
