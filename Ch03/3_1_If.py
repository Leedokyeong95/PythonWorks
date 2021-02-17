"""
날짜 : 2021/02/17
이름 : 이도경
내용 : 파이썬 조건문 실습 교재 p.60
"""

#If -> if문에서 print시 들여써야함(들여있는 공간이 if공간), 조건 끝에는 :(클론)
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 < num2:
    print('num1은 num2보다 크다.')

if num1 > 0: #중첩
     if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')

#If ~ else
num3, num4 = 3, 4

if num3 > num4:
    """조건이 참 일때"""
    print('num3이 num4보다 크다.')
else:
    """조건이 거짓 일때"""
    print('num3이 num4보다 작다.')

#If ~ elif ~ else

if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

#연습문제

score = input('점수 입력 :') #input에 입력하는 것은 숫자가 아닌 문자열이다.

score = int(score) #숫자변환해주는 함수
#score += 1 문자열이어서 불가능

if score >= 90 and score <= 100:
    """ 90 ~ 100 """
    print('A 입니다.')
elif score >= 80 and score < 90:
    """ 80 ~ 89 """
    print('B 입니다.')
elif score >= 70 and score < 80:
    """ 70 ~ 79 """
    print('C 입니다.')
elif 60 <= score< 70:
    """ 60 ~ 69 """
    print('D 입니다.')
elif 50 <= score < 60:
    """ 50 ~ 59 """
    print('E 입니다.')
elif score < 50:
    """ 0 ~ 50 """
    print('F 입니다.')

print('score :', score)

#교재 P63 삼항 조건문
#(1) 일반 조건문
num = 9 #초기화
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print('result :', result)

#(2) 3항 연산자
#형식) 변수 = 참 if(조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)
