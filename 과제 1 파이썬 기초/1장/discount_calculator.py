price = int(input("상품 가격을 입력해주세요: "))
dis = int(input("할인율을 입력해주세요(%): "))

disp = int(price*(dis/100))

print("원래 가격: %d"%price)
print(f"할인율: {dis}%")
print(f"할인 금액: {disp}")
print(f"최종 가격: {price-disp}")