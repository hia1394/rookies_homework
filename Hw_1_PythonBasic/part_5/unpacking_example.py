tu = (10,20)
list1 = [1,2,3]

x,y = tu
a,b,c = list1

def result(*args):
    return sum(args)

sum = result(10,20,30)

def result2(**kwargs):
    for key,value in kwargs.items():
        print()
print(f"좌표: X={x}, y={y}")
print(f"리스트 언패킹: a={a},b={b},c={c}")
print(f"가변 인수의 합: {sum}")

def result2(**kwargs):
    print("키워드 인수들: ",end="")
    for key,value in kwargs.items():
        print(f"{key} = {value}",end=",")
result2(name="김철수",age=25,city="서울")