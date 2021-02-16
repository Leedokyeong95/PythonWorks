"""
날짜 : 2021/02/16
이름 : 이도경
내용 : 파이썬 리스트 자료구조 실습하기
"""

#리스트 생성 [원소]
list1 = [1, 2, 3, 4, 5]

print('list1 type :', type(list1))
print('list1[0] :', list1[0])
print('list1[2] :', list1[2])
print('list1[4] :', list1[4])

list2 = [5, 3.14, True, '홍길동']

print('list2 type :', type(list2))
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])
print('list2[3] :', list2[3])

list3 = [[1, 2, 3], [True, False, True], ['김유신', '김춘추', '장보고']] #리스트 안에 리스트가 있는 것,행렬과 비슷

print('list3[0][2] :', list3[0][2])
print('list3[1][1] :', list3[1][1])
print('list3[2][0] :', list3[2][0])

#리스트 덧셈
animal1 = ['사자', '호랑이', '코끼리']
animal2 = ['기린', '곰']

result = animal1 + animal2
print('result :', result)

#리스트 수정, 삭제, 추가 -> 원소 수정도 가능
numbers = [1, 2, 3, 4, 5]

numbers[1] = 7   #원소 1번째인 2를 7로 수정하겠다
print('numbers :', numbers)

numbers[2:3] = [8, 9] #2번째 원소에서 3번째 원소 전까지인 3을 8과9로 수정
print('numbers :', numbers)

numbers[1:3] = [] #1번째 원소에서 3번째 원소 전까지인 7과8을 삭제한다
print('numbers :', numbers)

numbers.append(3) #append는 덧붙인다는 의미
print('numbers :', numbers)

del numbers[0] #del은 제거한다는 의미
print('numbers :', numbers)







