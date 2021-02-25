"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 중첩 예외처리 예제 p.215
"""

# 유형별 예외처리
print('\n유형별 예외처리')
try:
    div = 1000 / 2.53
    print('div = %5.2f' %(div))
    div = 1000 / 0
    f = open('c:\\test.txt')
    num = int(input('숫자 입력 : '))
    print('num =', num)

# 다중 예외처리 클래스
except ZeroDivisionError as e:
    print('오류 정보: ', e)
except FileNotFoundError as e:
    print('오류 정보: ', e)
except Exception as e:
    print('오류 정보: ', e)

finally :
    print('finally 영역 - 항상 실행되는 영역')