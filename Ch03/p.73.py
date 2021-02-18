"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.73. list 자료구조 예
"""

import random

# (1) list에 자료 저장하기
lst = []
for i in range(10):
    r = random.randint(1,10)
    lst.append(r)

print('lst=', lst)

# (2) list에 자료 참조하기
for i in range(10):
    print(lst[i] * 0.25)


