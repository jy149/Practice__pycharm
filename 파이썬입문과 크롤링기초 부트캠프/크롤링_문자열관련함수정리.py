'''
문자열 관련 함수 알아보기
# 문자열에 있는 특정 문자 갯수 세기(count 함수)
# 문자열에 있는 특정 문자의 위치 알려주기 -> index 함수
    # error 가 안나오게끔 할 수 없을까? -> find함수. -> 해당 문자열에 문자가 없으면 -1 을 리턴함
# 문자열 사이에 다른 문자 넣기 join
# 문자열 앞뒤에 공백 지우기 strip, lstrip, rstrip
# 대소문자 변환 upper, lower
# 문자열 중 일부를 다른 문자로 바꾸거나, 삭제하기 replace
'''

# 문자열에 있는 특정 문자 갯수 세기(count 함수)
data = 'Dave David'
d = data.count('D')
dd = data.count('Da')
print(dd, d, end=' ')
print()

#연습문제1. string에 v는 몇번?
print(data.count('v'))
#연습문제2. string에 vid는 몇번?
print(data.count('vid'))

print()

# 문자열에 있는 특정 문자의 위치 알려주기 -> index 함수
string = 'Dave ID is dave'
si = string.index('D') # 가장 처음 나오는 index 번호
print(si)

si_ex1 = string.index('D')
#si_ex2 = string.index('x') # -> 문자열에 찾는 문자가 없으면 error
print(si_ex1)

# error 가 안나오게끔 할 수 없을까? -> find함수. -> 해당 문자열에 문자가 없으면 -1 을 리턴함
sf_ex1 = string.find('x')
print(sf_ex1)

if string.find('x') == -1:
    print('x 는 스트링에 없습니다.')
print()

# 문자열 사이에 다른 문자 넣기 join
string = "12345"
comma = ","
cj = comma.join(string) # 껴넣을 문자.join(문자열)
print(cj)

string_ex = "임진영"
dot_ex ="..."
cj_ex1 = dot_ex.join(string_ex)
print(cj_ex1)
print()

# 문자열 앞뒤에 공백 지우기
data = " Dave   "
ds = data.strip()
print(ds)

data2 = "           Dave  "
print(data2)
ds2 = data2.lstrip()
print(ds2)
ds3 = data2.rstrip()
print(ds3)

print()

data3 = "    999999999999999999999(Dave)888888888888888     "
data4 = "    999999999999999999999(D999 ave)888888888888888     "
ds4 = data3.strip(' 98()')
ds5 = data4.strip(' 98()')
print(ds4)
print(ds5)

print()

# 대소문자 변환
string = 'Dave'
u = string.upper()
l = string.lower()
print(u)
print(l)

print()

# 문자열 나누기 split()
string = "Dave goes to Korea"
sp = string.split() # default 는 스페이스, 변환은 리스트형태로 반환
sp = string.split(' ') # 명시 가능
print(sp)

sp2 = string.split()[3]
print(sp2)

string2 = "Dave/goes/to/Korea"
sp3 = string2.split('/')
print(sp3)

# ? string = "10,11,22,33,44"를 컴마(,)로 분리해서 리스트 변수를 만들어 각 값을 정수형 리스트 데이터로 넣기

# 1
string = "10,11,22,33,44"
a = string.split(',')
print(a)

b=[]
for i in range(len(a)):
    b.append(int(a[i]))
print(b)

# 2
string = "10,11,22,33,44"
sp = string.split(',')
for i, sps in enumerate(sp):
    sp[i] = int(sps)
print(sp)

# 문자열 중 일부를 다른 문자로 바꾸거나, 삭제하기
string = "David goes to Korea"
sr = string.replace("David", "Jinyoung") # David 를 Jinyoung으로 바꾸기
print(sr)

string2 = " (Dave) "
sr2 = string2.replace("()","") # 이런식으로 해봤자 replace는 특정 문자그 sequence 자체를 하나의 문자로 보기때문에 괄호가 하나씩 지워지지는 않음
print(sr2)

sr2 = string2.replace("(","").replace(")","") # 이런식으로 한글자씩 지운것을 덮어서 다시 replace하자
print(sr2.strip())

#ex
string = "10,11,22,33,44"
sr_ex=string.replace(",","/")
print(sr_ex)


