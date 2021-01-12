# https://davelee-fun.github.io/blog/crawl_test

'''
꿀팁 1. F12 누르고 크롬 개발자 모드로 들어가자.
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

titles = soup.find_all('li', 'course')
for title in titles:
    print(title.get_text())

print()
print()
print()

'''
꿀팁 2. 추출한 것에서 또 추출하기
- find()로 더 크게 감싸는 HTML 태그로 추출하고
- 다시 추출된 데이터에서 find_all()로 원하는 부분 추출!
-> 추출된 데이터는 객체(Object)이다!
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

section = soup.find('ul', id='dev_course_list')
titles = section.find_all('li', 'course')
for title in titles:
    print(title.get_text())

print()
print()
print()

'''
꿀팁 3. 파이썬 문자열 함수와 함께 쓰기 (pre-processing)
- strip() 함수
- split() 함수
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

section = soup.find('ul', id='dev_course_list')
titles = section.find_all('li', 'course')
for index, title in enumerate(titles):
    print(str(index + 1) + '.',title.get_text().split('[')[0].split('-')[-1].strip())
# split으로 리스트 만들어가지고 선택, 선택,,, 그러다가 strip() 함수 쓰면됌
print()
print()
print()

# CSS Selector 사용하기(find / find_all 대체)
# hobby_course_list > li:nth-child(5)
# -> copy -> Copy Selector

'''
CSS Selector 사용!
- select() 안에 태그 또는 CSS class 이름 등을 넣음
- 결과 값은 리스트 형태로 반환! 
    - 매칭되는 첫번째 데이터만 얻고자 할 때는 select_one(), 이 땐 객체가 return

find() -> select_one()
find_all() -> select()
'''
# 기본
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('h3')
for item in items:
    print(item.get_text())
print()
print()

# 하위 태그 선택!
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

# items = soup.select('ul li') # 하위 태그를 나타낼 때는 띄어쓰기 해준다!
#items = soup.select('ul a') # 하위 태그를 나타낼 때는 띄어쓰기 해준다!
items = soup.select('ul > li') # 꺽쇠표시 구분은 앞선 태그 바로밑! 다음태그 데이터만 가져오겠다는 뜻
for item in items:
    print(item.get_text())
print()
print()


# css class 이름으로 검색
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

#items = soup.select('.course') #.class_name
#items = soup.select('#start') # #id_name
items = soup.select('.course.paid') ## 여러개의 클래스이름? -> .class_name.class_name.class_name ....

for item in items:
    print(item.get_text())
print()
print()


# 복합사용
print('복합사용')
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

# items = soup.select('ul#hobby_course_list > li.course')
items = soup.select('ul#dev_course_list > li.course.paid')
for item in items:
    print(item.get_text())
print()
print()

# 기본 ( select_one )
print('기본 ( select_one )')
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')

item = soup.select_one('ul#dev_course_list > li.course.paid')
a = item.get_text()
print(a)
print()
print()

# '추출한 것에서 추출하기 find()와 select() 비교'
print('추출한 것에서 추출하기 find()와 select() 비교')
from bs4 import BeautifulSoup
import requests

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html') # table 추가
soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('tr') # 행
for item in items:
    columns = item.select('td') # 열
    row_str = ''
    for column in columns:
        row_str += ',' + column.get_text()
    print(row_str[1:])
print()




print()
print()