# 3. 반복문
# while and for

# 1. while 문
i = 1
result = 0
while i <= 9: # i 가 9 보다 작거나 같을 때 아래 코드를 반복적 실행
    result += 1
    i += 1
print(result)

# 반복문안에서 i 가 홀수일때만 result에 더하기
i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# 2. for 문
# range(시작값, 끝값+1)
result = 0
for i in range(1, 10):
    result += i
print(result)

# range 시작값 default 는 0
scores = [90, 85, 77, 65, 97]
print(len(scores))
print(list(i for i in range(5)))
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다")
print('*'*100)
# 반복문 안의 continue -> continue를 만나게 되면 반복문 처음으로 돌아가게됌
scores = [90, 85, 77, 65, 97]
cheating_list = set([2, 4])

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다")
print('*'*100)

# 2중 반복문, 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()
print('*'*100)

