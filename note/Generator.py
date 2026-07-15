#生成器是一个特殊类型的迭代器
def plus_minus(x):
    yield x
    yield -x

t=plus_minus(3)
print(next(t))
print(next(t))

def evens(start,end):
    even=start+(start%2)
    while even<end:
        yield even
        even+=2

t=evens(7,15)
for i in t:
    print(i)

def countdown(k):
    if k>0:
        yield k
        yield from countdown(k-1)

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def list_partitions(n,m):
    if n<0 or m==0:
        return []
    else :
        exact_match=[]
        if n==m:
            exact_match=[[m]]
        with_m=[p+[m] for p in list_partitions(n-m,m)]
        without_m=list_partitions(n,m-1)
        return exact_match+with_m+without_m