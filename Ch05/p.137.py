"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 일획득자와 지정자 예제 p.137
"""

# (1) 중첩함수 정의
def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value

    return getter, setter

# (2) 외부 함수 호출
getter, setter = main_func(100)

# (3) 획득자 호출
print('num =', getter())

# (4) 지정자 획득
setter(200)
print('num =', getter())



















