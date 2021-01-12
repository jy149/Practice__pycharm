# 크롤링해서 엑셀 파일로 만들기!
'''
openpyxl 라이브러리 활용
'''
import openpyxl # 라이브러리 임포트
excel_file = openpyxl.Workbook() # openxl 라이브러리의 Workbook 호출. -> 엑셀파일 생성
# 엑셀 파일 생성 -> 디폴트 쉬트 생성, 엑셀파일변수.active 로 sheet 선택.
# sheet 이름 변경 -> title 변수 값을 변경
excel_sheet = excel_file.active
excel_sheet.title = 'test_sheet'

# 데이터 추가하기 -> 간단하게 엑셀파일변수.append([,]) 하면 리스트형태로 들어감.
# append 를 한번 호출하면 첫번째 row, 다음 호출시 다음 row로 append.
excel_sheet.append(['row1', 'data1', 'data2'])
excel_sheet.append(['row2', 'data3', 'data4'])

# 엑셀 파일 저장
excel_file.save('test.xlsx') # 인자로는 이름.

# 엑셀 파일 닫기
excel_file.close()




############################################
# 엑셀 파일 함수로 작성해서 만들기
############################################
import openpyxl

def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    excel_sheet.column_dimensions['A'].width = 100 # 엑셀 칸 늘리기
    excel_sheet.column_dimensions['B'].width = 20 # 엑셀 칸 늘리기

    if sheetname != '':
        excel_sheet.title = sheetname

    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename)
    excel_file.close()

############################################
# 크롤링한거 자동 만들기 -> 상품명 / 날짜
import requests
from bs4 import BeautifulSoup

product_lists = list()

for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('div.card')
    for item in data:
        product_name = item.select_one('div.card-body h4.card-text')
        product_date = item.select_one('div.wrapfooter span.post-date')
        product_info = [product_name.get_text().strip(), product_date.get_text()] # 날짜, 시고저종이면 여기 5개쓰면 될듯 / 그리고 get_value() 쓰면 될듯
        product_lists.append(product_info)

write_excel_template('test.xlsx', '상품정보', product_lists)










