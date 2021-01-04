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

'''














