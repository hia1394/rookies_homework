import csv

grades = [('김철수', 85),('이영희', 92),('박민수', 78),('최수진', 95)]

with open("grades.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grades)
    print("학생 성적이 grades.csv에 저장되었습니다.")

with open("grades.csv", 'r') as file:
    reader = csv.reader(file)  

    sum = 0
    cnt = 0
    print("성적분석 결과:")

    for i in reader:
        name,score = i
        score = int(score)
        print(f"{name}: {score}점")
        sum += score
        cnt += 1

result = sum/cnt
print(f"전체 평균: {result:.2f}")