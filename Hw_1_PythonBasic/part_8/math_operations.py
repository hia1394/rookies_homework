import math

def cir(r):
    return round(math.pi *r **2,2)
def rec(len,wid):
    return len*wid
def fac(i):
    result = 0 
    for i in range(1,i+1):
        result *= i
    return result
def gdc(a,b):
    while b:
        a,b=b,a%b
    return a