print("파일에 저장할 내용:")
print("안녕하세요")
print("파이썬 파일 처리를 연습하고 있습니다")
print("오늘은 좋은 날씨입니다")

with open("text.txt", 'w', encoding='utf-8') as file:
    file.write("안녕하세요\n")
    file.write("파이썬 파일 처리를 연습하고 있습니다\n")
    file.write("오늘은 좋은 날씨입니다\n")

with open("text.txt", 'r', encoding='utf-8') as file:
    content = file.read()  
    print("파일에서 읽어온 내용:")
    print(content)
