def fac_for(x):
    fac = 1
    for i in range(1,x+1):
        fac = fac*i
    return fac

def fac_re(y):
    if y==1:
        return 1
    else:
        return y*fac_re(y-1)

print(f"5!(재귀) = {fac_re(5)}")
print(f"5!(반복) = {fac_for(5)}")
print(f"7!(재귀) = {fac_re(7)}")
print(f"7!(반복) = {fac_for(7)}")