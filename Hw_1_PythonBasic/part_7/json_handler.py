import json

info ={"이름":"김철수","나이":25,"직업":"개발자","취미":["독서","영화감상","코딩"],"주소":"서울시 강남구"}

with open("data.json",mode='w') as file:
    json.dump(info, file)
    print("데이터가 data.json에 저장되었습니다.")

with open("data.json",mode='r') as file:
    data = json.load(file)
    print("JSON에서 읽어온 데이터: ")
    for key,value in data.items():
        print(f"{key}: {value}")