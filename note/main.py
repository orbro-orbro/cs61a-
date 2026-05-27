from math import sqrt

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
    return x>0 and sqrt(x)>30  #如果x是负数，那么根本不会报错，因为计算左值的时候，为False，不会进入第二个表达式

print(has_big_sqrt(10000))
print(has_big_sqrt(20))
print(has_big_sqrt(-1000))