"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 일급함수와 함수 클로저 예제 p.134
"""

# (1) 일급 함수
def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b
b = a()
b()

# (2) 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataSet = data
    #inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부 함수 호출
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)












