from collections import Counter
import re
with open("word.txt",'r',encoding='utf-8') as file:
    word = file.read()
    words = re.findall(r'\b\w+\b', word.lower())
    cnt = Counter(words)

    print("단어 빈도 분석 결과: ")
    for words,cnt in cnt.items():
        print(f"{words}: {cnt}번")