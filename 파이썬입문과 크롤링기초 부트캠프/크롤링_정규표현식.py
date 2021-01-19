'''
정규표현식 1.
'''

# 예제: 왜 정규표현식이 필요할까?
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

res = urlopen('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res, "html.parser")

data = soup.select('ul#dev_course_list li.course')
for item in data:
    print(item.get_text())

print()

# 가져온 크롤링 문자에서 뒤에 댓글을나타내는[1] 이런부분을 지워버리자.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

res = urlopen('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res, "html.parser")

data = soup.select('ul#dev_course_list li.course')
for item in data:
    print(re.sub('\[[0-9]+\]', '', item.get_text())) # 이 코드에서 '\[[0-9]+\]' -> 이부분이 [412]와 같은 부분의 정규표현식이며, '' 이거로 대체해서 나타내라는 뜻
    
print()
'''
세 라인의 코드를 추가하면 이름의 특징을 추출할 수 있음
import re
regex = re.compile('[A-Za-z]+\.')
print(regex.findall('찾을문자열')
'''
# titanic data 정규표현식으로 추출

import openpyxl
import re

regex = re.compile('[A-Za-z]+\.') # 정규표현식은 패턴화된 부분을 표현할 수 있음.
# 엑셀 파일 열기
work_book = openpyxl.load_workbook('train.xlsx')

# 현재 Active Sheet 얻기
work_sheet = work_book.active

# work_sheet.rows는 해당 쉬트의 모든 행을 객체로 가지고 있음
for each_row in work_sheet.rows:
    print(each_row[3].value)
    print(regex.findall(each_row[3].value))
work_book.close()



