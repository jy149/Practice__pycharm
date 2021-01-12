################################################
# list
location = ['서울시', '경기도', '인천시']
print(location[0])
print(location[1:3])
location.append('부산시')
print(location)
location.append('대전시')
print(location)
print(location[2:5])

# list에서 삭제
print(location)
print(type(location.remove('경기도')))
print(location)
del location[0]
print(location)

# 삽입
print(location)
location.insert(1,'경기도')
print(location)

#
location = []
location.append('서울시')
location.append('경기도')
print(location)
print(location[1])

#
print(location)
location[1] = '부천시'
print(location)
print()

# 리스트 변수
'''
1. 리스트 선언
- 리스트 변수 = []
- 리스트 변수 = list()

2. 리스트 추가
- 리스트 변수.append(데이터)
- 리스트 변수.insert(인덱스번호, 데이터)

3. 리스트 삭제
- 리스트변수.remove(데이터)
- del 리스트변수[인덱스번호]

4. 리스트 데이터 수정
- 리스트변수[인덱스번호] = 수정할 데이터
'''

# 리스트 데이터 정렬하기
numbers = [2, 1, 4, 3]
print(numbers)

numbers.sort()
print(numbers)
 # 리스트 데이터 역순 정렬
numbers = [2, 1, 4, 3]
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)

print()

#
python_is_easy = "python is easy"
a = python_is_easy.split()
print(a)
print(python_is_easy)






