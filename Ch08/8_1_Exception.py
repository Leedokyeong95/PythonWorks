"""
날짜 : 2021/02/24
이름 : 이도경
내용 : 파이썬 예외처리 실습하기 교재 p.212
"""

# try ~ except -> 예외가 발생해도 출력가능하게 함
if __name__ == '__main__':
    num1, num2 = 1, 0
    r1 = r2 = r3 = r4 = 0

    try:
        r1 = num1 + num2
        r2 = num1 - num2
        r3 = num1 * num2
        r4 = num1 / num2

    except:
        print('예외 발생...')

    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)




# try ~ except ~ finally
if __name__ == '__main__':

    people = ['김유신', '김춘추', '장보고']

    try:
    # try는 예외가 발생할 가능성이 있는 로직 영역
        for i in range(4):
            print(peole[i])

    except:
    # 예외가 발생했을 때 처리할 로직 영역
        print('유효하지 않은 인덱스 사용...')

    finally:
    # 예외가 발생여부에 관계없이 마지막에 실행되는 영역
        print('예외처리 완료...')




# try ~ except ~ else
if __name__ == '__main__':

    animal = ['사자', '코끼리', '호랑이', '기린']
    result = None

    while True:
        try:
        # try는 예외가 발생할 가능성이 있는 로직 영역
            print('동물을 선택하세요.')
            print('1:사자, 2:코끼리, 3:호랑이, 4:기린, 0:종료')

            answer = input('선택 : ')
            answer = int(answer)

            if answer == 0:
                break

            result = animal[answer-1] # 리스트 번호는 0부터 시작이라서 마이너스 1

        except:
        # 예외가 발생했을 때 처리할 로직 영역
            print('정확히 숫자를 다시 입력하세요.')

        else:
        # 예외가 발생 안 했을 때 처리할 로직 영역
            print('선택한 동물 :', result)

    print('프로그램 종료...')
