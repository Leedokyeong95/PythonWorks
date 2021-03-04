"""
날짜 : 2021/03/04
이름 : 이도경
내용 : 파이썬 데이터베이스 SQL 실습
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='ldk',
                       password='1234',
                       db='ldk',
                       charset='utf8') #한글문자를 쓴다는 utf8

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
sql = "INSERT INTO `USER1` VALUES ('p101', '김유신', '010-1234-1001', 25);" #나이는 따옴표 안함
cur.execute(sql)

# 실행 확정
conn.commit()

# 데이터베이스 접속 종료
conn.close()

print('INSERT 완료...')



