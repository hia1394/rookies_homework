em = input("이메일 주소를 입력하세요: ")

kw = em.find("@")
print(f"사용자명: {em[:kw]}")
print(f"도메인명: {em[kw+1:]}")