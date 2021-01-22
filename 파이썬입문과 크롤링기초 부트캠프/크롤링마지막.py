# 크롤링 프로그램 완성 : 크롤링한 데이터에서 다시 크롤링하기1
# divide and conquer -> 굉장히 복잡한 문제를 작은 문제로 쪼개서 전체를 완성하자

# 크롤링한 것을 크롤링하자! 새로운기술

# 1. G마켓 크롤링하기 - BeautifulSoup 과 requests
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')
'''

# 2 타이틀과 실제 판매 금액을 크롤링하기! ( 전체 먼저 뽑고 그안에서 다시 크롤링 )
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')

bestlists = soup.select('div.best-list') # .class_name
bestitems = bestlists[1]
products = bestitems.select('ul > li')

for i, product in enumerate(products):
    title = product.select_one('a.itemname')
    price = product.select_one('div.s-price > strong')
    print(i+1, title.get_text(), price.get_text())
'''
# 3. 기능 추가 # 상품을 어떤 업체가 제공했을까? # 클릭으로 들어가서 크롤링 한부분에 대해서 다시 크롤링 하기
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')

bestlists = soup.select('div.best-list') # .class_name
bestitems = bestlists[1]
products = bestitems.select('ul > li')

for i, product in enumerate(products):
    title = product.select_one('a.itemname')
    price = product.select_one('div.s-price > strong')

    # 크롤링 안의 크롤링 requests.get 을 다시 해줌!
    res_info = requests.get(title['href']) # title['href']#마치 사전 구조처럼 되어있음
    soup_info = BeautifulSoup(res_info.content, 'html.parser')
    provider_info = soup_info.select_one('div.item-topinfo.item-topinfo--additional > div.item-topinfo_headline > p > span.text__seller > a')

    print(i+1, title.get_text(), price.get_text(), provider_info.get_text())
'''
# 4. 엑셀파일까지 만들어보자.
import requests, openpyxl
from bs4 import BeautifulSoup

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.append(['랭킹','상품명','판매가격','상품상세링크','판매업체'])

excel_sheet.column_dimensions['B'].width = 80
excel_sheet.column_dimensions['C'].width = 30
excel_sheet.column_dimensions['D'].width = 80
excel_sheet.column_dimensions['E'].width = 30

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')

bestlists = soup.select('div.best-list') # .class_name
bestitems = bestlists[1]
products = bestitems.select('ul > li')

for i, product in enumerate(products):
    title = product.select_one('a.itemname')
    price = product.select_one('div.s-price > strong')

    # 크롤링 안의 크롤링 requests.get 을 다시 해줌!
    res_info = requests.get(title['href']) # title['href']#마치 사전 구조처럼 되어있음
    soup_info = BeautifulSoup(res_info.content, 'html.parser')
    provider_info = soup_info.select_one('div.item-topinfo.item-topinfo--additional > div.item-topinfo_headline > p > span.text__seller > a')

    print(i+1, title.get_text(), price.get_text(),title['href'], provider_info.get_text())
    excel_sheet.append([i+1, title.get_text(), price.get_text(),title['href'], provider_info.get_text()])

    excel_sheet.cell(row = i + 2, column=4).hyperlink = title['href'] # 특정 셀을 하이퍼링크로 만들기

cell_A1 = excel_sheet['A1'] # 셀선택
cell_A1.alignment = openpyxl.styles.Alignment(horizontal='center') # 중앙정렬
cell_A1.font = openpyxl.styles.Font(color='01579B') # google material color palette # 폰트칼라

cell_B1 = excel_sheet['B1']
cell_B1.alignment = openpyxl.styles.Alignment(horizontal='center')
cell_B1.font = openpyxl.styles.Font(color='01579B') # google material color palette

cell_C1 = excel_sheet['C1']
cell_C1.alignment = openpyxl.styles.Alignment(horizontal='center')
cell_C1.font = openpyxl.styles.Font(color='01579B') # google material color palette

cell_D1 = excel_sheet['D1']
cell_D1.alignment = openpyxl.styles.Alignment(horizontal='center')
cell_D1.font = openpyxl.styles.Font(color='01579B') # google material color palette

cell_E1 = excel_sheet['E1']
cell_E1.alignment = openpyxl.styles.Alignment(horizontal='center')
cell_E1.font = openpyxl.styles.Font(color='01579B') # google material color palette

excel_file.save('Bestsproduct_com_Gmarket.xlsx')
excel_file.close()