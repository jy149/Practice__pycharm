##############################################################
# 1. 자료형
'''
수 자료형(Number)
- 정수와 실수
'''

# '정수형(Integer) / 양의 정수, 음의 정수, 0'
print('정수형(Integer) / 양의 정수, 음의 정수, 0')
a = 1000
b = -7
c = 0
print(a, b, c, end=' ')
print()
print()

# '실수형(Real Number) / 변수에 소수점을 붙이면 실수형 변수로 처리됨'
print('실수형(Real Number) / 변수에 소수점을 붙이면 실수형 변수로 처리됨')
a = 157.93
b = -1837.2
c = 5.
d = -.7
print(a, b, c, d, end=' ')
print()
print()

# 'e나 E를 활용한 지수 표현 방식'
print('e나 E를 활용한 지수 표현 방식')
# 1e9 -> 1,000,000,000
a = 1e9
b = 75.25e1
c = 3954e-3
print(a, b, c, end=' ')
print()
print()

# '실수형 사칙연산의 오류'
print('실수형 사칙연산의 오류')
# 이진법체계
a = .3+.6

if a == 0.9:
    print(True)
else:
    print(False)
print()
print()

# '위와 같은 오류는 round() 함수를 사용하자. / round(인자, 반올림하고자하는위치)'
print('위와 같은 오류는 round() 함수를 사용하자. / round(인자, 반올림하고자하는위치)')
a = round(123.456, 2) # 소수 3번째자리에서 반올림
print(a)
print()

a = .3 + .6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)
print()
print()

# '수 자료형의 연산'
print('수 자료형의 연산')
a = 7
b = 3
print(a / b) # 나누기
print(a // b) # 몫
print(a % b) # 나머지
print(a ** b) # 거듭제곱
print()
print()

# '리스트 자료형'
print('리스트 자료형')
'''
- 리스트는 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용
- append(), remove() 등의 method 사용
- 배열 혹은 테이블이라 부르기도.
'''

# '리스트 만들기'
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[4]) # 5번째 자리 출력
# 빈리스트 선언 1
a = list()
print(a)
# 빈리스트 선언 2
a = []
print(a)
print()

# 크기가 N인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
print()

# 리스트의 인덱싱과 슬라이싱
'''
- 리스트의 특정 원소에 접근하는 것을 인덱싱(Indexing)
- 음의 정수를 넣으면 원소를 거꾸로 탐색
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1]) # 리스트 뒤에서 첫번째 값 출력
print(a[-3]) # 뒤에서 세번째 값
a[3] = 7 # 네번째 위치 값 변경
print(a)
print()

'''
- 리스트의 연속적인 위치를 갖는 원소 가져오기 슬라이싱(Slicing)
- 대괄호에 콜론(:)을 이용 시작인덱스와 끝 인덱스 설정
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])
print()

# 중요!
# 리스트 컴프리헨션
'''
- 리스트를 초기화 하는 방법 중 하나
- 대괄호[] 안에 조건문과 반복문을 넣는 방식으로 초기화
'''
# 컴프리헨션 예제 1
array = [ i for i in range(1, 20) if i % 2 == 1] # 1부터 19까지 수 중에서 홀수만 출력
print(array)

# 위의 컴프리헨션 코드와 같은 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)
print()
print()

# 컴프리헨션 예제 2
array = [ i * i for i in range(1, 10)] # 1부터 9까지의 수를 제곱한 값들 출력
print(array)

# 컴프리헨션 예제 3. 2차원 리스트 초기화
# N X M 크기 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
print()

'''
# _ (언더바)의 역할
- 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 함 
'''
# 1
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

# 2
for _ in range(5):
    print('Hello Python')
print()

# 컴프리헨션 예제 3-1. 잘못된 2차원 리스트의 초기화
# N X M 크기 2차원 리스트를 잘못 초기화 하면 아래처럼 2차원 리스트를 생성하고 값을 변경할때
# 변경된 값이 동일 값으로 치환되어 의도한 바와 다른 결과가 나올 수 있음
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[0][1] = 5 # 첫번째 row 의 두번째 column 값만 바꾸고 싶었으나 모든 두번째 column 값이 바뀌게 되는 결과가 나옴
print(array)

# 리스트 관련 기타 메서드
'''
- append() / 변수명.append() - 리스트에 원소 하나 삽입
- sort() / 변수명.sort() , 변수명.sort(reverse=True) - 기본은 오름차순, reverse=True 옵션을 통해 내림차순
- reverse() / 변수명.reverse() - 리스트 원소 순서 뒤집기
- insert() / 변수명.insert(삽입위치인덱스, 삽입값) - 특정 인덱스 위치에 원소 삽입
- count() / 변수명.count(특정값) - 리스트에서 특정 값을 가지는 데이터 개수 셈
- remove() / 변수명.remove(특정값) - 특정값 갖는 원소 제거, 값을 가진 원소가 여러개면 하나만 제거. 
'''

















