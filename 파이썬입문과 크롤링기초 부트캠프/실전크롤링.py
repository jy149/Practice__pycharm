'''# 네이버 쇼핑 사이트 크롤링하기
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.shopping.naver.com/best100v2/main.nhn")
soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('#popular_srch_lst > li > span.txt')
for item in items:
    print(item.get_text())
print()
print()
print()
# 네이버 쇼핑 사이트 크롤링하기 - 패션의류 100
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000")
soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('#productListArea > ul > li > p > a')
for item in items:
    print(item.get_text())
print()
print()
print()
# 여러가지 싸이트 리스트
import requests
from bs4 import BeautifulSoup

site_list=["https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000", "https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000002"]

for site in site_list:
    res = requests.get(site)
    soup = BeautifulSoup(res.content, 'html.parser')
    items = soup.select('#productListArea > ul > li > p > a')
    print(site)
    for item in items:
        print(item.get_text())
print()
print()
print()
'''

'''
Naver 금융 크롤링
'''
import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/")
soup = BeautifulSoup(res.content, 'html.parser')

#items = soup.select('#popularItemList > li > a')
items = soup.select('div.rgt > ul.lst_major > li')

for item in items:
    print("지수이름:",item.find('a').get_text(),"현재지수:", item.find('span').get_text(),"등락:", item.find('em').get_text())
