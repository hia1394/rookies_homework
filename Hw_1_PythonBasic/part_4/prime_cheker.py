num = int(input("숫자를 입력하세요: "))

for i in range(num-2):
    if (num%(i+2))==0:
        print(f"{num}은 소수가 아닙니다.")
        break
else:
    print(f"{num}은 소수입니다.")