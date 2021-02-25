"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 1~n 정수 누적합 예제 p.142
"""

# (1) 재귀함수 정의 : 1~n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n == 1 :
        return 1
    else:
        result = n + Adder(n-1)

        print(n, end = ' ')
        return result


# (2) 함수 호출1
print('n=1 :', Adder(1))

# (3) 함수 호출2
print('\nn=5 :', Adder(5))











