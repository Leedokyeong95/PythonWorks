"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 숫자 카운트 예제 p.140
"""

# (1) 재귀함수 정의 : 1~n 카운트
def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)

# (2) 함수 호출1
print('n=0 : ', Counter(0))

# (3) 함수 호출2
Counter(5)

