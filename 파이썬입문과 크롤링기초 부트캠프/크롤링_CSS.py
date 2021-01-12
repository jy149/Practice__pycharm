# CSS 언어란???
'''
적용방법
- 적용할 태그에 style 속성으로 넣기
- HTML 문서 <head>안에 <style> 태그로 넣기
- HTML 문서 <head> 안에 CSS 파일로 링크하기
'''

# 크롤링 패턴 코드
'''
import requests
from bs4 import BeautifulSoup

res = requests.get("http://v.media.daum.net/v/20170615203441266")
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())
'''
import requests
from bs4 import BeautifulSoup

res = requests.get("http://v.media.daum.net/v/20170615203441266")
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find_all('span',class_='txt_info')
for item in mydata:
    print(item.get_text())
print(mydata[0].string)

# 기사의 맨 위에 부분 출력하기
data = soup.find('div', 'layer_util layer_summary') # 클래스가 2개이상일때도 그냥 띄어쓰기하고 쓰면 된다.
print(data.get_text()) # data.string 써도 됌

############
#크롤링 후처리
# * \n, 불필요한 데이터 삭제, 깔끔하게 문자열 정리 -> 파이썬 문자열처리로 정리.



