"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 함수 장식자 예제 p.138
"""

# (1) 래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요!')
        func()
        print('잘가요!')
    return decorated

# (2) 함수 장식자 적용
@wrap
def hello():
    print('hi ~ ', "홍길동")

# (3) 함수 호출
hello()




























