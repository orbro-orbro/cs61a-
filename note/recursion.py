def split(n):
    return n//10,n%10

def sum_digit(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return sum_digit(all_but_last)+last
    


def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1)
    
print(fact(4))