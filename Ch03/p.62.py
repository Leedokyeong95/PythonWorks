"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.62 중첩 조건문 예
"""

score = int(input('점수 입력 : '))
grade = '' #등급

if score >= 85 and score <= 100 :
    grade = '우수'
elif score >= 70 :
    grade = '보통'
else :
    grade = '저조'

print('당신이 점수는 %d이고, 등급은 %s'% (score, grade))