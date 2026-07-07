# ============================================================
# 数据抽象 (Data Abstraction)
# ============================================================

"""
数据抽象 = 将"数据怎么用"和"数据怎么存"分离。

核心思想：你只需要知道构造器和选择器，不需要知道底层实现。
  - 构造器 (Constructor)：创建/组装一个数据值
  - 选择器 (Selector)  ：从数据值中取出组成部分

类比：你开车只需要知道方向盘和油门（接口），
      不需要知道发动机怎么工作（实现）。

只要构造器和选择器的行为一致，底层实现可以随意替换，
使用该数据的所有代码完全不受影响。

后续两部分:Mutability(可变性)与 具体的抽象实现方式。
"""
def rational(n,d):      #constructor
    def select(name):
        if name=='n':
            return n
        elif name=='d':
            return d
    return select

def numer(x):           #selector
    return x('n')
def denom(x):
    return x('d')

def rational_siml(x1):  #化简
    Numer=numer(x1)
    Denom=denom(x1)
    i,Up=2,min(Numer,Denom)
    max_factor=1
    while i <=Up:
        if Numer%i==0 and Denom%i==0:
            max_factor=i
        i+=1
    return rational(Numer//max_factor,Denom//max_factor)

def rational_multi(x1,x2):  #乘法
    return rational_siml(rational(numer(x1)*numer(x2),denom(x1)*denom(x2)))

print(numer(rational_siml(rational(6,9))))
x1=rational(4,8)
x2=rational(6,153)
x3=rational_multi(x1,x2)
print(numer(x3),denom(x3))


