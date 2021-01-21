# 크롤링 프로그램 완성 : 크롤링한 데이터에서 다시 크롤링하기1
# divide and conquer -> 굉장히 복잡한 문제를 작은 문제로 쪼개서 전체를 완성하자

# 크롤링한 것을 크롤링하자! 새로운기술

import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')
