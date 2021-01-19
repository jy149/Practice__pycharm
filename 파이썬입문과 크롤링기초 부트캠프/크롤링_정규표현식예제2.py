# findall 함수 : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴
import re
pattern = re.compile('[a-z]+')
findalled = pattern.findall('Game of Life in Python')
print(findalled)

# 가장 많이 쓰이는 예제 -> 문자열에서 단어들 찾아내기.
pattern2 = re.compile('[A-Za-z]+')
findalled2 = pattern2.findall('Game of Life in Python')
print(findalled2)

# findall 함수를 사용해서 정규표현식에 해당되는 문자열이 있는지 없는지 확인하기
import re
pattern = re.compile('[a-z]+')
findalled = pattern.findall('GAME')
if len(findalled) > 0:
    print("정규표현식에 맞는 문자열이 존재함")
else:
    print("정규표현식에 맞는 문자열이 존재하지 않음")

print()

# split 함수 : 찾은 정규표현식 패턴문자열을 기준으로 문자열을 분리
import re
pattern2 = re.compile(':')
splited = pattern2.split('python:java')
print(splited)

# 예제 'VS'로 문자열 앞뒤 분리
#pattern_ex = re.compile('VS')
pattern_ex = re.compile(' [A-Z]{2} ')
splited_ex = pattern_ex.split('python VS java')
print(splited_ex)
