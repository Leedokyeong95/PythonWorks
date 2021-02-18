"""
날짜 : 2021/02/18
이름 : 이도경
내용 : 교재 p.65 while 반목문 예
"""

# (1) 카운터와 누적변수
cnt = tot = 0 #변수 초기화
while cnt < 5 : #True : loop 수행
    cnt += 1 # 카운터 변수(cnt = cnt + 1)
    tot += cnt # 누적변수 : tot = tot = cnt
    print(cnt, tot)

#[실습] 1 ~ 100 사이 3의ㅡ 배수 합과 원소 추출하기
cnt = tot = 0
dataset = [] # 빈 list

while cnt < 100: #100회 반복
    cnt += 1 #카운터
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print('1 ~ `00 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)





