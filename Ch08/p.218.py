"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 텍스트 파일 입출력 예제 p.218
"""

# (1) 현재 작업디렉터리
import os
print('\n현재 경로:', os.getcwd())

# (2) 예외처리
try :
    # (3) 파일 읽기
    ftest1 = open('chapter08/data/ftest.txt', mode = 'r')
    print(ftest1.read())

    # (4) 파일 쓰기
    ftest2 = open('Chapter08/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')

    # (5) 파일 쓰기 + 내용 추가
    ftest3 = open('chapter08/data/ftest2.txt', mode = 'a')
    ftest3.write('\nmy second text ~~~')
except Exception as e:
    print('Error 발생 : ', e)

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()