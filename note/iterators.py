# 可迭代对象(iterable): 可传给iter()的对象 — list, str, dict, range等
# 迭代器(iterator): iter()返回的对象，记住遍历位置，每次next()前进一步
# iter(iterable) → 创建迭代器
# next(iterator) → 返回下一个元素，耗尽时抛出 StopIteration
# for x in obj 本质 = iter() + 反复 next() + 捕获 StopIteration

s = [[1, 2], 3, 4, 5]
t = iter(s)
print(next(t))    # [1, 2]  ← 第一个元素
print(next(t))    # 3       ← 推进到第二个
print(list(t))    # [4, 5]  ← 消耗剩余（同一迭代器，不含前两个）

# next() 和 list() 都在消耗同一个迭代器 — 走了两个就只剩两个
# 迭代器是"一次性"的：耗尽即空，重新遍历需重新 iter()
# 惰性求值：按需产生元素，range(10**9) 可正常迭代而不会爆内存
# 后续：map/filter/zip 返回迭代器；生成器(yield)是最常用的创建方式

s=[1,2,3]
t=iter(s)
t2=iter(s)
q=map(lambda x:x*x,t)#产生一个新的迭代器，元素是func(elem)
f=filter(lambda x:x>1,t2)#产生一个新的迭代器，只保留predicate为True的元素
z=zip([1,2],[3,4])#产生一个新的迭代器，元素是各iterable对应位置元素的元组，最短耗尽即停
r=reversed(s)#产生一个新的迭代器，以逆序产出序列的元素（接受sequence，非任意iterable）
print(next(r))

# 易错：多个惰性迭代器(map/filter/zip等)共享同一底层迭代器时，消费其一即掏空底层，其余迭代器只能拿到剩余（或空）数据


def func(x):
    print('3*',x,'=',3*x)
    return 3*x
m=map(func,[3,4,5])

t=filter(lambda y:y>11,m)
print(next(t))
print(next(t))
#next(t)第三个next报错：第一个元素func后是9，不纳入t中


# 生成器函数(yield): 有yield的函数返回生成器(一种迭代器)，惰性产出
def gen():
    yield 1
    yield 2
g = gen()
next(g)  # 1，执行到第一个yield暂停，局部变量/执行位置全部保留
next(g)  # 2，从上次暂停处恢复
# 生成器表达式: (x*x for x in range(5)) — 惰性版列表推导，不占内存

# 迭代器自身也是可迭代对象: iter(t) is t → True
# 所以迭代器可直接for循环 — 但只能走一遍，耗尽即空

# for x in obj 的三步拆解:
# t = iter(obj)
# while True:
#     try: x = next(t)
#     except StopIteration: break
