"""
날짜 : 2021/02/16
이름 : 이도경
내용 : 파이썬 튜플 자료구조 실습하기
"""

#Tuple 생성
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2, 3, 4, 5
tuple3 = ('한국', '미국', '일본', '중국', '호주')

print('tuple1 type:', type(tuple1))
print('tup1e2 type:', type(tuple2))
print('tup1e3 type:', type(tuple3))

print('tuple1[0] :', tuple1[0])
print('tuple2[2] :', tuple2[2])
print('tuple3[0] :', tuple3[0])
print('tuple3[1] :', tuple3[1])
print('tuple3[0] : %s' % tuple3[0])
print('tuple3[1] : %s' % tuple3[1])

#Tuple 원소 수정, 삭제 불가능
#tuple1[0] = 7 불가능
#del tuple2[1] 불가능
#print('tuple1[0] :', tuple1[0])
