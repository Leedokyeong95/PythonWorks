"""
날짜 : 2021/02/22
이름 : 이도경
내용 : 파이썬 모듈 패키지 실습하기 교재 p.114
"""
#import = 출처
import Ch05.lib.Calc as cal #cal이라고 하겠다.

rs1 = cal.plus(1, 2)
rs2 = cal.minus(1, 2)
rs3 = cal.multi(2, 3)
rs4 = cal.div(4, 2)

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)
print('rs4 :', rs4)
##########################
from Ch05.lib.Calc import * # *는 all *(=plus, minus, multi, div)
r1 = plus(2, 3)
r2 = minus(3, 1)
r3 = multi(4, 3)
r4 = div(8, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)


