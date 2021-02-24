"""
날짜 : 2021/02/24
이름 : 이도경
내용 : 파이썬 파일 입출력 실습하기 교재 p.217
"""

# 파일 읽기
file = open('C:/Users/user/Desktop/Sample.txt', 'r') #'r' : 읽기모드
line = file.readline()

print('line :', line) #한줄만 읽음
file.close()

# 멀티라인 파일 읽기
file = open('C:/Users/user/Desktop/Sample.txt', 'r')

while True:
    line = file.read()

    if not line: #라인이 없으면
        break

    print('line :', line)

file.close()

# 파일 쓰기
sample2 = open('C:/Users/user/Desktop/Sample2.txt', 'w') # w(write) : 쓰기 모드
sample2.write('안녕하세요.\n') #\n은 띄어쓰기
sample2.write('반갑습니다.\n')
sample2.write('감사합니다.\n')
sample2.close()

# 구구단 쓰기

gugudan = open('C:/Users/user/Desktop/gugudan.txt', 'w')

for x in range(2, 10):

    gugudan.write('%d단\n'% x)

    for y in range(1, 10):

        z = x * y
        gugudan.write('%d X %d = %d\n'% (x, y, z))

gugudan.close()






