"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.67 random 관련 함수1 예
"""


# (1) random module 추가
import random
help(random)

# (2) random module의 함수 도움말
help(random.random)

# (3) 0~1 사이 난수 실수
r = random.random()
print('r=', r)

#[실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True :
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1

print('난수 개수 = ', cnt)












