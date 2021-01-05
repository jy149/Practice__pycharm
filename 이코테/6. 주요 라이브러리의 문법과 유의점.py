# 6. 주요 라이브러리의 문법과 유의점
'''
# 표준 라이브러리란?
- 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
- # 6가지는 꼭 알고 있자
- print(), input(), sorted() -> 내장 함수
- itertools / 반복 형태 데이터 처리, 순열 및 조합 라이브러리
- heapq / 힙(Heap)기능 제공, 우선순위 큐 기능 구현
- bisect / 이진 탐색(Binary Search)  기능 제공
- collections / 덱(deque), 카운터(Counter) 등의 자료구조 포함 라이브러리
- math / 필수 수학기능 라이브러리, 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이 등
'''

# 내장함수 print(), input(), sum(), min(), max(), eval(), sorted()
result = sum([1, 2, 3, 4, 5])
result = min(7, 3, 5, 2)
result = max(7, 3, 5, 2)

result = eval("(3+5) * 7") # eval 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식 계산 결과를 반환

result = sorted([9, 1, 8, 5, 4])
result = sorted([9, 1, 8, 5, 4], reverse=True)
result = sorted([('A', 35), ('B', 75), ('C', 50)], key = lambda x : x[1], reverse = True) # key 값을 x의 두번째 원소값으로 reverse 하여 sort

result = [9, 1, 8, 5, 4]
result.sort()
result.sort(reverse=True)
print(result)
print()

# itertools.
# permutations, combinations

# permutations - 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산
# list ['A', 'B', 'C'] 에서 3개를 뽑아 나열하는 모든 경우 출력
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# combinations - 조합 계산(중복허용 X)
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# product - 순열계산(중복허용 O)
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement - 조합계산(중복허용 O)
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)
print()

# 힙이란??
# https://blog.tomclansys.com/56
# heapq
# 힙 원소 삽입 -> heapq.heappush()
# 힙에서 원소 추출 -> heapq.heappop()
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable: # 모든 원소를 차례로 힙에 삽입
        #print(h)
        #print(result)
        heapq.heappush(h, value)
        #print(h)
        #print(result)
        #print()
    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        #print(h)
        #print(result)
        result.append(heapq.heappop(h))
        #print(h)
        #print(result)
        #print()
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 내림차순 힙정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable: # 모든 원소를 차례로 힙에 삽입
        heapq.heappush(h, -value) # -value
    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(-heapq.heappop(h)) # -heapq
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)





