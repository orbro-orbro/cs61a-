a=1
def f(g):
    a=2
    return lambda y:a*g(y)

print(a)
print(f(lambda y:a+y)(a))#这里的a都是global的
print(a)

#return语句会切回父级的frame，并且不会执行该函数体
def search(f):
    x=0
    while True:
        if f(x):
            return x
        x+=1

def square(x):
    return x*x
def inverse(f):
    """返回 f 的反函数：给定 y,从 0 开始暴力搜索最小的 x 使 f(x)==y。
    前提:f 定义在非负整数上，且为单射。若不存在这样的 x 则死循环。"""
    return lambda y:search(lambda x:f(x)==y)

sqrt=inverse(square)
print(sqrt(16))

def pivate(x):
    def ok(x):
        return x
    return ok
print(pivate(2)(square)(4))#第一个参数2传入pivate函数，和内置的ok函数不存在关系
#换而言之，无论pivate（m），m为任意值，均得到一个ok函数（等值函数）


print('逆天')
def horse(mask):
    horse=mask
    def mask(horse):
        return horse
    return horse(mask)

mask=lambda horse:horse(2)
print(horse(mask))
#一坨大便
# === 执行流程（帧视角） ===
# 全局帧: horse→<func line37>, mask→λ1(line43)
# f1 horse(λ1): horse=λ1, mask=恒等函数 → return λ1(恒等函数)
# f2 λ1(恒等函数): 恒等函数(2)
# f3 恒等(2): return 2
# 逐层返回 → print(2)


def trace(fn):
    def wrapped(x):
        print(1)
        result=fn(x)
        print(2)
        return result
    return wrapped

@trace
def square(x):
    return x*x
print(square(3))