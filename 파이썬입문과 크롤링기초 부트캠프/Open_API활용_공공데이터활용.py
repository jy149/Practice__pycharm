'''
공공데이터포탈 data.go.kr
# Python 샘플 코드 #
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10',
quote_plus('pageNo') : '1', quote_plus('stationName') : '종로구', quote_plus('dataTerm') : 'DAILY', quote_plus('ver') : '1.3' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body
'''
'''
http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getMsrstnList?addr=서울&stationName=종로구&pageNo=1&numOfRows=10&ServiceKey=lV%2B4%2Fc4BkVasgTO9dW%2Fsch5gDXNu8Df7ErZ%2Bi6uWYpfkP5Vqog%2Be0l9SPxET5zRyALoEvAXaf%2BPh%2FgnZZXePzg%3D%3D
'''

import requests
from bs4 import BeautifulSoup

service_key = 'lV%2B4%2Fc4BkVasgTO9dW%2Fsch5gDXNu8Df7ErZ%2Bi6uWYpfkP5Vqog%2Be0l9SPxET5zRyALoEvAXaf%2BPh%2FgnZZXePzg%3D%3D'
params = '&numOfRows=10&pageNo=1&stationName=도봉구&dataTerm=DAILY'
open_api = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?ServiceKey=' + service_key + params

res = requests.get(open_api)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
for item in data:
    datatime = item.find('datatime')
    o3value = item.find('o3value')
    print(datatime.get_text(), o3value.get_text())