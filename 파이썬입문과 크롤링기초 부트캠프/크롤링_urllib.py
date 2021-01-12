'''
기존에는 urllib + bs4
-> 최근에는 requests + bs4
'''
# 1. requests 라이브러리로 작성한 코드
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/')
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('h4.card-text')
for item in data:
    print(item.get_text().strip())
print()
print()

# 2. urllib 라이브러리로 작성한 코드 # requests.get -> urlopen / res.content -> res
from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen('https://davelee-fun.github.io/')
soup = BeautifulSoup(res, 'html.parser')

data = soup.select('h4.card-text')
for item in data:
    print(item.get_text().strip())
print()
print()

'''
HTTP response code
- 페이지가 없는경우?? 확인 방법!
# 응답코드? -> requests.get().status_code 에 존재!
'''

import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/xxx') # 이 페이지는 없는페이지임!
if res.status_code != 200:
    print('페이지 없음')
else:
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('h4.card-text')
    for item in data:
        print(item.get_text())
print()
print()

'''
여러 페이지를 크롤링 하는 방법! -> 반복문을 쓰자
'''
import requests
from bs4 import BeautifulSoup

for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('h4.card-text')
    for item in data:
        print(item.get_text().strip())






