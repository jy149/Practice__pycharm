for i in range(10):
    print(i, end=' ')
print()

# 1부터 10까지 합하기
_sum = 0
for i in range(1, 11):
    _sum += i
print(_sum)

# while 문
i = 0
while i <= 3:
    print(i)
    i += i+1

# while문 2
'''
name = ''
while name != "foo bar":
    name = input("What's your name?")
    print("Hi, ", name, "So, where is foo bar?")
'''
