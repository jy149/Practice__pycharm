# 크롤링 핵심 코드 패턴으로 이해하기
# 필요 라이브러리 설치
# requests : 웹페이지 가져오기 라이브러리
# bs4(BeautifulSoup) : 웹페이지 분석(크롤링)라이브러리

'''
import requests
from bs4 import BeautifulSoup
res = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())
'''

# 라이브러리 임포트
import requests
from bs4 import BeautifulSoup # 대문자로 된거 보니까 BeautifulSoup 은 Class지

# 웹페이지 가져오기
res = requests.get('http://v.media.daum.net/v/20170615203441266') # 원하는 페이지를 requests 라이브러리에 get이라는 method에 넣어주기만 하면 됌 인자는 웹페이지 주소.
#print(res.content) # res.content 메소드를 출력하게 되면 html로 이루어진 파일의 내용이다! (ctrl+u 를 누르면 웹페이지 소스를 볼 수 있음)

'''
문자열의 의미를 분석하는 것을 파싱! 이라고 한다.
<html>
    <head>
    </head>
    <body>
    </body>
</html>
이러한 분석작업을 대신 해주는, 대신 파싱해줌! -> bs4
'''

# 웹페이지 파싱하기
soup = BeautifulSoup(res.content, 'html.parser') # 첫번째 인자가 분석할 content이다. parser가 여러가지 있는데 기본적인 html.parser를 써주면 된다.
#print(soup)

# 필요한 데이터 추출하기
print(soup.find('h3'))
print(soup.find('title'))

data1 = soup.find('h3')
mydata = soup.find('title')

# 추출한 데이터 활용하기
print(data1.get_text())
print(mydata.get_text())


# HTML / CSS / Javascript
'''
- <HTML 이란?>
HTML 은 마크업 언어이다. ( 문서나 데이터의 구조를 표현하는 언어 ), 웹페이지를 만드는 언어이다.
<tag> Hello HTML </tag> -> <태그> 로 시작, </태그> 로 끝 (동일 태그 이름)
<b> -> 이런 태그 같은경우는 내용을 볼드체로 써라 라는 태그.

- html 기본 구조
<!DCOTYPE html> -> 이 문서는 HTML 파일이다~ 라는 태그
<html> -> 이 태그 다음부터 나오는 코드들은 HTML언어로 시작이 된다~ 라는 뜻
<head> -> 문서 전체의 정보를 head 태그 안에 써줌.(예를들어 제목)
</head>
<body> -> 화면에 표시되는, 문서의 실제 내용 시작부분이다.
</body>
</html> -> 닫기

-살펴보기
- <title>HTML test</title> -> title 태그는 head 안에 들어감 -> 본문의 내용은 아니지만 웹페이지의 제목을 나타낸다!
- <meta charset="utf-8"> -> 웹브라우저로 HTML을 오픈했는데 글자가 깨지면 head 태그안에 해당 태그를 써넣으면됌!
- <img src="dimg.png" width="100" height="100"> -> 이미지를 표현하는 태그, 태그(img) <속성이름(src)=속성값("dimg.png")> 속성(attribute) 속성과 속성사이는 한 칸 띄움
- <br> -> 이것은 엔터!
- id= "~" -> 속성의 id

HTML 주요 태그들
# https://developer.mozilla.org/ko/docs/Web/HTML/Element
'''
# 패턴으로 실습하며 익히기: HTML 이해를 바탕으로 크롤링하기.
from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"
soup = BeautifulSoup(html, "html.parser")
#태그로 검색 방법
# data = soup.find('h1') # 여기 .find method에 어떤 인자를 넣을 것인지가 핵심!
# data = soup.find('body') # None
data = soup.find('p')

print(data)
print(data.string)
print(data.get_text())
print()

'''
HTML 언어 이해를 기반으로 크롤링!
- p 태그 문장이 두 개인데 이 중에 하나를 선택하려면?? -> 속성을 선택해서 뽑아내보자
data = soup.find('p', class_='cssstyle')
data = soup.find('p', 'cssstyle')
data = soup.find('p', attrs={'align':'center'})
data = soup.find(id='body')
'''

from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"
soup = BeautifulSoup(html, "html.parser")
data = soup.find('p', attrs={'id':'body', 'align':'center'})
print(data.string)
print()

################
from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"
soup = BeautifulSoup(html, "html.parser")
data = soup.find('p') # 가장 첫번째만 가져오게 된다. -> 특정조건에 해당하는 모든 것을 찾길 원함! -> find_all
print(data)
# find_all 을 쓸때에는 for문을 써서 string으로 표현해준다.
data1 = soup.find_all('p')
print(data1, type(data1))
for item in data1:
    print(item.string)



