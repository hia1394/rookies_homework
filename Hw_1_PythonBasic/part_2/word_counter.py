str = input("문장을 입력하세요: ")

str2 = ' '.join(str.split())
print(f"공백 제거 {str2}")
print(f"단어 개수: {len(str2.split())}")