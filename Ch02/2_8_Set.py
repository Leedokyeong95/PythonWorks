"""
날짜 : 2021/02/16
이름 : 이도경
내용 : 파이썬 집합 자료구조 실습하기
"""

#집합 생성 -> 중복불가, 순서 고려 안됨
set1 = set([1, 2, 3, 4, 5, 3, 1])
set2 = set('Hello Korea')
#중복이 안되므로 문자가 7개만 들어 있음

print('set1 :', set1)
print('set2 :', set2)

#집합 출력(리스트로 변환)
set1_list = list(set1)
set2_list = list(set2)

print('set1_list[0] :', set1_list[0])
print('set1_list[1] :', set1_list[1])
print('set1_list[2] :', set1_list[2])
#숫자는 랜덤이지만 순서대로 나오고
print('set2_list[0] :', set2_list[0])
print('set2_list[1] :', set2_list[1])
#문자는 할때마다 랜덤임