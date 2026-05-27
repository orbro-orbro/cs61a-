from math import sqrt,pi
from operator import mul
#def real_sqrt(x):
#    return  if_(x>=0,sqrt(x),0) #这么写是错误的，因为在传参中会calculate sqrt(x),

def if_(c,t,f):
    if c:
        return t
    else:
        return f


#print(real_sqrt(-5))

#and or,
#and:先计算左值，如果是False，就直接结束，输出False；如果是True，结果由第二个表达式决定
#or：先计算左值，如果是True，直接结束，输出True；如果是False，结果由第二个表达式决定
def has_big_sqrt(x):
    return x>0 and sqrt(x)>30

print(has_big_sqrt(10000))
print(has_big_sqrt(20))
print(has_big_sqrt(-1000))

def resonable(n):#检验这个数字是否合理
    return n==0 or 1/n!=0 #先计算左值，n如果极大，1/n 等于0，这个数字判断为不合理

print(resonable(10**1000))
print(resonable(0))


print('New Note')
#assert 3>2
#assert 2>3,'Amazing'
#assert：如果后面的表达式为True就无事发生，如果不是则 ！报错！,并输出后面自己输入的报错信息
def area(r,shape_constant):
    assert r>0,'A length should be positive'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)


#求和
def summation(n,term):    #term绑定的是通项公式（本质是函数）
    total,k=0,1
    while k<=n:
        total,k=term(k)+total,k+1
    return total

def cube(k):#三次项
    return pow(k,3)
t=5
print(summation(t,cube))

#收敛到pi
def pi_term(k):
    return 8/mul(4*k-3,4*k-1)

print(summation(10,pi_term))


#使用函数创建函数
def make_adder(n):
    def adder(k):
        return k+n
    return adder

f=make_adder(5)#输入数字+5
print(f(10))
#or
print(make_adder(5)(10))