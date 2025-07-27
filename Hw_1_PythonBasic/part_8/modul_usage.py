import datetime
import random

now = datetime.datetime.now()
fm_date = now.strftime('%y년 %m월 %d일 %a')
num = 7
flo = 3.14
fruit = ['사과','바나나','오렌지','딸기','포도']
random.shuffle(fruit)

print(f"현재 날짜와 시간: {now}")
print(f"포맷된 날짜: {fm_date}")
print(f"임의의 숫자: {num}")
print(f"임의의 실수: {flo}")
print(f"임의의 리스트 요소: {random.choice(fruit)}")
print(f"섞인 리스트: {fruit}")