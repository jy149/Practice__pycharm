# 정규표현식 예제
# 예제 : 문자, 숫자가 아닌 데이터를 찾아서, ''로 대체하라(삭제하라)
import re
string = " (Dave) "
sr = re.sub('[^A-Za-z0-9]', '', string) #정규표현식 읽기# ^ (꺽쇠) : 아닌 / A-Z까지 a-z까지 0-9 까지
print(sr)

# replace로도 할 수는 있음
print(string.replace('(','').replace(')','').strip())

print()
'''
regular expression
- [0-9] : \d : 숫자를 찾음
- [^0-9] : \D : 숫자가 아닌 것을 찾음(텍스트, 특수 문자, white space(스페이스, 탭, 엔터 등등)를 찾을 때)
- [\t\n\r\f\v] : \s : white space(스페이스, 탭, 엔터 등등) 문자인 것을 찾음
- [^\t\n\r\f\v] : \S : white space(스페이스, 탭, 엔터 등등) 문자가 아닌 것을 찾음(텍스트, 특수문자, 숫자를 찾을 때)
- [A-Z-a-z0-9] : \w : 문자, 숫자를 찾음
- [^A-Z-a-z0-9] : \W : 문자, 숫자가 아닌 것을 찾음
'''

# 정규표현식 1. Dot.
# Dot. 메타 문자는 줄바꿈 문자인 \n 을 제외한 모든 문자(한 개)를 의미
# D.A 는 D + 모든 문자(한 개) + A 를 의미
#   - DAA, DvA, D1A
import re
pattern = re.compile('D.A')
print(pattern.search("DAA"))
print(pattern.search('D1A'))
# 패턴이 찾아지지 않으면(D와 A사이에 문자가 한개만 들어가야됌) None
print(pattern.search('D00A'))
print(pattern.search('DA'))
print(pattern.search('d0A'))

print(pattern.search('d0A D1A 0111')) # span 4~7 위치가 매칭된다.

print()

# 정말 Dot . 이 들어간 패턴을 찾으려면?
# \. 으로 표시하거나 [.] 으로 표시.
pattern = re.compile('D\.A')
print(pattern.search("D.A"))
print(pattern.search("DDA"))
print(pattern.search("D[.]A"))

print()

# 앞선 search 코드는 정규표현식에 들어가있는지 확인하는 코드임.
# 예제를 보자
# 찾고 바꾸기 (특정 패턴이 매칭되는 것을 찾아서, 다른 문자열로 바꾸기)
string = "DDA D1A DDA DA"
a = re.sub('D.A', 'Jinyoung', string) # re.sub(패턴, 바꿀데이터, 원본데이터)
print(a)
