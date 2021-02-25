"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 함수 스코프 예제 p.132
"""

# (1) 지역변수 예
x = 50 #전역변수
def local_func(x):
    x += 50 #지역변수 -> 종료 시점 소멸
local_func(x)
print('x =', x)

# (2) 전역변수 예
def golbal_func():
    global x #전역변수 x 사용
    x += 50

golbal_func()
print('x= ', x)



