import math_operations as math_op

r = 5
cir = math_op.cir(r)
print(f"원의 넓이{cir:.2f}")

len = 10
wid = 5
rec = math_op.rec(len,wid)
print(f"직사각형의 넓이: {rec}")

i = 5
fac = math_op.fac(i)
print(f"팩토리얼 {i}! = {fac}")

a = 48
b = 18
gdc = math_op.gdc(a,b)
print(f"최대공약수({a},{b}) = {gdc}")