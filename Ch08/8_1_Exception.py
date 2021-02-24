"""
날짜 : 2021/02/24
이름 : 이도경
내용 : 파이썬 예외처리 실습하기 교재 p.212
"""

# try ~ except -> 예외가 발생해도 출력가능하게 함
if __name__ == '__main__':
    num1, num2 = 1, 0

    try:
        r1 = num1 + num2
        r2 = num1 - num2
        r3 = num1 * num2
        r4 = num1 / num2

    except:
        print('예외 발생...')

    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)


# try ~ except ~ finally


# try ~ except ~ else