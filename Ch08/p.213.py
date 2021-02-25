"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 간단한 예외처리 예제 p.213
"""

# (1) 예외 발생 코드

print('프로그램 시작 !!!')
x = [10, 30, 25.2, 'num', 14, 51]

for i in x:
    print(i)
    y = i ** 2
    print('y =', y)

print('프로그램 종료')


# (2) 예외 처리 코드
print('프로그램 시작 !!!')

for i in x:
    try :
        y = i ** 2
        print('i=', i, ', y =', y)
    except :
        print('숫자 아님 :', i)

print('프로그램 종료')