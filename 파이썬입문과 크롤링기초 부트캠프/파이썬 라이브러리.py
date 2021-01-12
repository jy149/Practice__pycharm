# 파이썬 라이브러리
# 라이브러리 : 미리 만들어놓은 함수 집합, 이름이 있음

# 지수승 구하기
print(3 ** 3)

#함수로 만들기
def exponential(digit, exponent):
    value = digit ** exponent
    return value
print(exponential(3, 3))

# 이러한 수학 함수들을 모아놓은 라이브러리 -> math
import math
num = math.pow(3, 3) # 지수승 pow
print(num, type(num))

pac = math.factorial(5)
print(pac)


# math 라이브러리에 있는 함수 중, sqrt, factorial 함수만 import
from math import sqrt, factorial
num = sqrt(5)
print(num)
num2 = factorial(5)
print(num2)

# 다음과 같이 쓰면 해당라이브러리에 존재하는 모든 함수를 라이브러리 명 없이 사용 가능
from math import *
num = sqrt(5) + factorial(3)
print(num)

# 라이브러리, 함수 명이 너무 길어서 바꾸고 싶음
import math as m
num = m.factorial(4)
print(num)

from math import factorial as f
num = f(4)
print(num)

# ctrl + art + s -> project interpreter
from googletrans import Translator
T = Translator()
word = T.translate('안녕하세요', dest='en', src = 'ko')
print(word.text)

