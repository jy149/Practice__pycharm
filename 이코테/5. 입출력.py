# 5. 입출력
'''
- 파이썬에서 데이터를 입력받을 때는 input()
- 정수형 데이터로 처리하기 int()
- 여러개의 데이터 입력받기 -> list(map(int, input().split()))
'''

#
'''
n = int(input()) # 데이터 갯수입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
'''

#
'''
n, m, k = map(int, input().split())
print(n, m, k)
'''

# 입력을 빨리받기, input 이 아니라 sys 라이브러리르 사용
import sys
# sys.stdin.readline().rstrip() # readline으로 입력하면 엔터가 줄 바꿈 기호로 입력됌, 이 공백문자를 제거하기 위해 rstrip() 사용

# readline() 사용 소스코드
# 문자열 입력
#data = sys.stdin.readline().rstrip()
#print(data)

# 문자열 출력
answer = 7
# print('정답 :' + answer + '입니다.') 에러
print('정답 :' + str(answer) + ' 입니다.')

# f-string
print(f"정답은 {answer} 입니다")




