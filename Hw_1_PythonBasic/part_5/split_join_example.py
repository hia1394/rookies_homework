str = ("Python is awesome programming language" )
str2 = str.split()
str3 = "-".join(str2)
str4 = str.upper()

print(f"원본 문자열: {str}")
print(f"분리된 단어들: {str2}")
print(f"하이픈으로 연결: {str3}")
print(f"대문자로 변환 후 공백으로 연결: {str4}")