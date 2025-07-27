student = ['김철수','이영희','박민수','최수진']
scores = [85,92,78,95]

print("학생과 점수 매칭: ")
for st,sc in zip(student,scores):   
    print(f"{st}: {sc}점")