fruit = ['사과','바나나','오렌지','포도','딸기']

print(f"과일 목록: {fruit}")


fi = input("찾을 과일을 입력하세요: ")

try:
    fruit.index(fi)
    print(f"\'{fi}\'가 목록에 있습니다.")
except:
    print(f"\'{fi}\'가 목록에 없습니다.")
