"""
날짜 : 2021/02/25
이름 : 이도경
내용 : 파이썬 프로그램 문자열 치환 예제 p.198
"""

from re import sub
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# (1) 특수문자 제거
text1 = sub('[\^*$]+', '', st3)
print(text1)

# (2) 숫자 제거
text2 = sub('[0-9]', '', text1)
print(text2)