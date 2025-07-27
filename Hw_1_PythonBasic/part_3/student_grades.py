grades = {'김철수':85,'이영희':92,'박민수':78,'최수진':95}

g_sum = sum(grades.values())
print(f"학생 성적: {grades}")
print(f"평균 점수: {g_sum/len(grades)}")