'''
Open API(Rest API)란?
API : Application Programming Interface의 약자로, 특정 프로그램을 만들기 위해 제공되는 모듈(함수 등)을 의미
Open API : 공개 API라고도 불리우며, 누구나 사용할 수 있도록 공개된 API
Rest API : Representational State Transfer API의 약자. HTTP 프로토콜을 통해 서버 제공 기능을 사용할 수 있는 함수를 의미
    - 일반적으로 XML, JSON의 형태로 응답 전달.

postman -> download ( openAPI 작동되는지 바로 확인하는 거 )

JSON 포멧 예
{ "id::"01", "language": "Java", "edition": "third", "author": "Herbert Schildt"}
-> dict 형식과 동일하다.{"key": "Value",...}
value 안에는 리스트로 들어가도됌 [{"":"", "":"",...}]

json.loads(data) -> parsing 하는거임
'''


import json
# 네이버 쇼핑에서, android 라는 키워드로 검색한 상품 리스트 결과
data = """
{
    "lastBuildDate": "Mon, 18 Jan 2021 10:16:28 +0900",
    "total": 23269,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "라온시큐어, MDM 솔루션 국내 최초 美 구글 추천 제품 등재",
            "originallink": "https://www.etoday.co.kr/news/view/1985440",
            "link": "https://www.etoday.co.kr/news/view/1985440",
            "description": "이투데이=고종민 기자 | ICT 통합보안 선도기업 라온시큐어가 자사의 스마트워크 보안 플랫폼 ‘원가드(OneGuard)’가 구글의 ‘안드로이드 엔터프라이즈 솔루션 디렉토리(<b>Android</b> Enterprise Solutions Directory)’에... ",
            "pubDate": "Mon, 18 Jan 2021 10:04:00 +0900"
        },
        {
            "title": "라온시큐어 MDM 솔루션, 美 구글 추천 제품 선정",
            "originallink": "http://www.newspim.com/news/view/20210118000222",
            "link": "http://www.newspim.com/news/view/20210118000222",
            "description": "ICT 통합보안 선도기업 라온시큐어(대표 이순형)는 자사의 스마트워크 보안 플랫폼 '원가드(OneGuard)'가 구글의 '안드로이드 엔터프라이즈 솔루션 디렉토리(<b>Android</b> Enterprise Solutions Directory)'에 등재됐다고 18일... ",
            "pubDate": "Mon, 18 Jan 2021 10:02:00 +0900"
        },
        {
            "title": "라온시큐어 'MDM 솔루션', 美구글 추천제품 선정",
            "originallink": "http://www.fnnews.com/news/202101180949136923",
            "link": "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=014&aid=0004566878",
            "description": "라온시큐어는 자사의 스마트워크 보안 플랫폼 ‘원가드(OneGuard)’가 구글의 ‘안드로이드 엔터프라이즈 솔루션 디렉토리(<b>Android</b> Enterprise Solutions Directory)’에 등재됐다고 18일 밝혔다. 이는 국내 MDM(Mobile... ",
            "pubDate": "Mon, 18 Jan 2021 09:53:00 +0900"
        },
        {
            "title": "라온시큐어 MDM 솔루션, 美 구글 추천 제품 선정",
            "originallink": "http://www.marketnews.co.kr/news/articleView.html?idxno=59699",
            "link": "http://www.marketnews.co.kr/news/articleView.html?idxno=59699",
            "description": " 라온시큐어는 자사의 스마트워크 보안 플랫폼 '원가드(OneGuard)'가 구글의 '안드로이드 엔터프라이즈 솔루션 디렉토리(<b>Android</b> Enterprise Solutions Directory)'에 등재됐다고 18일 밝혔다. 이는 국내 MDM... ",
            "pubDate": "Mon, 18 Jan 2021 09:51:00 +0900"
        },
        {
            "title": "[포토] 또다시 서울 눈… 지난 6일보다 더 온다",
            "originallink": "http://newsclaim.co.kr/View.aspx?No=1419308",
            "link": "http://newsclaim.co.kr/View.aspx?No=1419308",
            "description": "또한 추돌사고 등의 피해가 발생하지 않도록 보행자 안전과 교통안전에 유의해야 한다고 덧붙였다. /data/user/0/com.samsung.<b>android</b>.app.notes/files/clipdata/clipdata_bodytext_210117_222904_537.sdocx",
            "pubDate": "Mon, 18 Jan 2021 01:56:00 +0900"
        },
        {
            "title": "The Sunday Read: ‘The Valve Turners’",
            "originallink": "https://www.nytimes.com/2021/01/17/podcasts/the-daily/valve-turners-climate-activists.html?partner=naver",
            "link": "https://www.nytimes.com/2021/01/17/podcasts/the-daily/valve-turners-climate-activists.html?partner=naver",
            "description": "To hear more audio stories from publishers like The New York Times, download Audm for iPhone or <b>Android</b>. There are a lot of ways to listen to ‘The Daily.’ Here’s how. We want to hear from... ",
            "pubDate": "Sun, 17 Jan 2021 23:04:00 +0900"
        },
        {
            "title": "[포토] 대설 예비특보 하얗게 변한 길거리, 최고 15㎝ 많은 눈 예상",
            "originallink": "http://newsclaim.co.kr/View.aspx?No=1419309",
            "link": "http://newsclaim.co.kr/View.aspx?No=1419309",
            "description": "또한 추돌사고 등의 피해가 발생하지 않도록 보행자 안전과 교통안전에 유의해야 한다고 밝혔다. /data/user/0/com.samsung.<b>android</b>.app.notes/files/clipdata/clipdata_bodytext_210117_223045_569.sdocx",
            "pubDate": "Sun, 17 Jan 2021 22:36:00 +0900"
        },
        {
            "title": "A message to LG Electronics",
            "originallink": "https://www.koreatimes.co.kr/www/tech/2021/01/133_302606.html",
            "link": "https://www.koreatimes.co.kr/www/tech/2021/01/133_302606.html",
            "description": "Except for die-hard Apple fans, the ecosystem Samsung has established would probably be suitable for fans of the <b>Android</b> operating system. Because the smartphone industry is currently dominated... ",
            "pubDate": "Sun, 17 Jan 2021 19:16:00 +0900"
        },
        {
            "title": "현대차 아반떼 '2021 북미 올해의 차' 수상",
            "originallink": "http://www.chungnamilbo.co.kr/news/articleView.html?idxno=580916",
            "link": "http://www.chungnamilbo.co.kr/news/articleView.html?idxno=580916",
            "description": "파라메트릭 다이내믹스 디자인을 테마로 한 드라마틱한 4도어 쿠페 룩이 살아있으며, 세그먼트 최초로 무선 애플 카플레이(Apple CarPlay™) 와 안드로이드오토(<b>Android</b> Auto™), 현대 디지털 키 등 첨단 기능을... ",
            "pubDate": "Sun, 17 Jan 2021 13:19:00 +0900"
        },
        {
            "title": "WhatsApp Delays Privacy Changes Amid User Backlash",
            "originallink": "https://www.nytimes.com/2021/01/15/technology/whatsapp-privacy-changes-delayed.html?partner=naver",
            "link": "https://www.nytimes.com/2021/01/15/technology/whatsapp-privacy-changes-delayed.html?partner=naver",
            "description": "1 app in India, one of WhatsApp’s biggest markets, on Apple and <b>Android</b> phones. Now, WhatsApp executives are assuring users that its changes are minor, that it cannot read users’ messages and... ",
            "pubDate": "Sat, 16 Jan 2021 04:31:00 +0900"
        }
    ]
}
"""
json_data = json.loads(data)
print(json_data)
print(json_data["lastBuildDate"])
print(json_data["items"][0]['title'])
print(json_data["items"][0]['link'])

print()
print()


# 파이썬 코드로 naver openapi 가져오기
print("파이썬 코드로 naver openapi 가져오기")
import requests
import pprint # pprint.pprint() 로 출력하면 좀더 구조적으로 출력 쌉가능

client_id = '77dhvEQYUb57IC1W2u8j'
client_secret = '2Bjqxuk_Pn'

naver_open_api = 'https://openapi.naver.com/v1/search/news.json?query=컨설팅'
header_params = {"X-Naver-Client-Id" : client_id, "X-Naver-Client-Secret" : client_secret}
res = requests.get(naver_open_api, headers = header_params) # headers는 http라는 규약, 특정주소에 header라는 특정 정보가 들어가 있음

#data = res.json() # .json() 을 사용해주면 구조화된 json 형태로 보여주게 됌.
#print(data)

# 크롤링 결과가 정상적인지 아닌지를 판단해줌 .status_code == 200 : -> 200이면 정상적으로 판단된것이다.
if res.status_code ==200:
    data = res.json()
    #for item in data['items']:
    for index, item in enumerate(data['items']):
        print(index + 1, item['title'], item['link'])
else:
    print("Error Code:", res.status_code)

# print(res.text) -> 이런것도 있음


print()
print()
print()









