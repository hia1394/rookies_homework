score = 85
age=17
num = [-1,-3,-5,1,2,4,6]

result = "합격" if score >=80 else "불합격"
stat = "성인" if age>19 else "미성년자"
max_num = max(num)
check = [nums for nums in num if nums>0]

print(f"점수: {score}, 결과: {result}")
print(f"나이: {age}, 상태: {stat}")
print(f"숫자들의 최대값: {max_num}")
print(f"양수들: {check}")
