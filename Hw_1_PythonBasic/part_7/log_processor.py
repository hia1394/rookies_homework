import logging

logging.basicConfig(filename='data.log',level=logging.DEBUG, encoding='utf-8',format='%(asctime)s - %(levelname)s - %(message)s',\
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.error("데이터베이스 연결 실패")
logging.error("파일을 찾을 수 없습니다.")
logging.warning("메모리 사용량이 높습니다.")
logging.warning("디스크 공간 부족")

print("로그 파일이 생성되었습니다")

print("ERROR 레벨 로그들: \n")
with open('data.log',mode='r',encoding='utf-8') as file:
    for msg in file:
        if "ERROR" in msg:
            print(msg)

print("WARNING 레벨 로그들: \n")
with open('data.log',mode='r',encoding='utf-8') as file:
    for msg in file:
        if "WARNING" in msg:
            print(msg)