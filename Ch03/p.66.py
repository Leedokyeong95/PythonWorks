"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.66 무한 루프(loop) 예
"""

# 무한 루프(loop)
numData = []

while True :
    num = int(input("숫자 입력 : "))

    if num % 10 == 0 :
        print("프로그램 종료")
        break
    else :
        print(num)
        numData.append(num)








