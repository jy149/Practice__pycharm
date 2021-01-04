# 2. 조건문
x = 15
if x >= 10:
    print(x)

# if ~ elif ~ else 구문 사용
############################################
print()
score = 85
if score >= 90:
    print('학점 : A')
elif score >= 80:
    print('학점 B')
elif score >= 70:
    print('학점 : C')
else:
    print('학점 F')
############################################
print()
score = 85
if score >= 70:
    print('성적이 70점 이상입니다')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70미만입니다.')
    print('분발하세요')
print('프로그램 종료')
############################################

'''
비교 연산자
==, !=, >, <, >=, <=

논리 연산자
X and Y (둘 모두 참일때 참), X or Y (둘중 하나 참일때 참), not X (X가 거짓일때 참) 

기타 연산자
X in Y, X not in Y / Y = list, tuple, chr, num, dict ..
'''
print()
# pass 사용법
score = 85
if score >= 80:
    pass # 나중에 작성할 소스 코드
else:
    print('성적이 80점 미만')
print('프로그램 종료')
print()
#######################################
# 실행될 소스코드가 한 줄일 경우
score = 85
if score >= 80: result = 'Success'
else: result = 'Fail'
print(result)
print()
#######################################
# 조건부 표현식(Conditional Expression)
score = 85
result = "Success" if score >= 80 else 'Fall'
print(result)
#######################################
# ex) 리스트에서 특정한 원소의 값만을 없앤다고 가정.
#1. 일반적 코드
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = set([3,5])
print(type(remove_set))
result = []
for i in a:
    if i not in remove_set:
        result.append(i)
print(result)

# 2. 간단한 코드
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = set([3,5])
result = [i for i in a if i not in remove_set]
print(result)
print()














