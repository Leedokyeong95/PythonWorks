"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.43 표준입력장치 예
"""

# (1) 문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type :', type(num))
print('num =', num)
print('num =', num*2)

# (2) 문자형 숫자를 정수형으로 변환
num1 = int(input("숫자 입력 : ")) # str -> int
print('num1 = ', num1*2)

# (3) 문자형 숫자를 실수형으로 변화
num2 = float(input("숫자 입력 : ")) # str -> float
result = num1 + num2 #실수 = 정수 + 실수
print('result =', result)


