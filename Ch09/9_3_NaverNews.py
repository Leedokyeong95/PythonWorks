"""
날짜 : 2021/03/08
이름 : 이도경
내용 : 파이썬 네이버 뉴스 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# 네이버 뉴스 요청하기

resp = req.get('https://news.naver.com/main/home.nhn', headers={'User-Agent': 'Mozilla/5.0'})
# print(resp.text)

# 헤드라인 뉴스 제목 5건 파싱
#5개 기사를 한번에 뽑으면서 각가 뽑을때
#dom.select와 for를 사용해야함

dom = bs(resp.text, 'html.parser')
tags_a = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')

for a in tags_a:
    print(a.text.strip()) #strip : 공백제거

# 네이버 속보 뉴스 크롤링
page = 1

# Excel 파일생성
workbook = Workbook()
sheet = workbook.active


while True :
    print('page:', page)
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20210308&page='+str(page)
    #마지막 page는 숫자라서 에러가 안나려면 문자열로 바꿔줘야함
    resp = req.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    dom = bs(resp.text, 'html.parser')

    tag_tits = dom.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2) > a')

    for tit in tag_tits:
       # print('tit : ', tit.text.strip())
        sheet.append([tit.text.strip()])
    page += 1

    if page > 10:
        break

# Excel 파일저장
workbook.save('C:/Users/user/Desktop/News.xlsx')
workbook.close()

print('크롤링 완료...')

