"""
날짜 : 2021/02/22
이름 : 이도경
내용 : 파이썬 내장함수 실습하기 교재 p.115
"""
#기본
import time #파이썬의 기본 모듈
import math, random

# time 함수
t1 = time.time()
print('t1 :', t1)

t2 = time.ctime()
print('t2 :', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일'% (year, month, date))
print('%s시 %s분 %s초'% (hour, min, sec))

# abs 함수 - 절대값
r1 = abs(-5)
print('r1 :', r1)

# ceil 함수 - 올림함수인데 math라는 모듈이 필요함, math모듈은 위에
r2 = math.ceil(1.2)
r3 = math.ceil(1.8)

print('r2 :', r2)
print('r3 :', r3)

# floor 함수 - 내림함수
r4 = math.floor(1.2)
r5 = math.floor(1.8)

print('r4 :', r4)
print('r5 :', r5)

# round 함수 - 반올림함수, 내장함수라서 math모듈이 필요없음
r6 = round(1.2)
r7 = round(1.8)

print('r6 :', r6)
print('r7 :', r7)

# random 함수(중요), 임의의 수, 모듈 필요
num1 = random.random()
print('num1 :', num1) # 0 ~ 1 사이의 실수

num2 = num1 * 10
print('num2 :', num2) # 0 ~ 10 사이의 실수

num3 = math.ceil(num2)
print('num3 :', num3) # 1 ~ 10 사이의 실수

#한번에 실행
result = math.ceil(random.random() * 10)
print('result :', result) # 1 ~ 10 사이의 실수


result = math.ceil(random.random() * 45)
print('result :', result) # 로또 랜덤
