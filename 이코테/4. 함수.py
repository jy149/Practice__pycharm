# 4. 함수
# 더하기 함수
def add(a, b):
    return a + b
print(add(3,4))

# return 없이 함수 안에서 출력하게끔
def add(a, b):
    print('함수결과:', a + b)
add(3, 4)

# argument를 직접 지정하기
def add(a, b):
    print('함수결과:', a + b)
add(b = 3, a = 4)

# 함수에서 지역 변수를 활용하지 않고 global 변수로 지정하여 함수 바깥의 선언된 변수 참조하기
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)

# 람다 표현식
def add(a, b):
    return a + b
print(add(3, 7)) # 일반 식

print((lambda a, b: a + b)(3, 7))


