grade = int(input("점수를 입력하세요:"))


if grade>=90:
    rate = 'A'
elif grade>=80:
    rate = 'B'
elif grade>=70:
    rate = 'C'
elif grade>=60:
    rate = 'D'
else:
    rate = 'F'

print(f"점수 {grade}점의 학점은 {rate}입니다.")