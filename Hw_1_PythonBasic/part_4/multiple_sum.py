num = []
for i in range(99):
    if (i+1)%3==0:
        num.append(i+1)
sum =0 
print(f"1부터 100까지 3의 배수: {num}")
for i in num:
    sum += i
print(f"3의 배수의 합: {sum}")
print(f"3의 배수의 개수: {len(num)}개")