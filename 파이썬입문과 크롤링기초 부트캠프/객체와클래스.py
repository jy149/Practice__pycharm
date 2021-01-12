# 객체지향 프로그래밍(Object Oriented Programming)

# 1. 두 함수의 차이는?
def print_string(data):
    print(data)
print_string("Fun Coding")

string = "Fun Coding"
a = string.split()
print(a)

'''
절차지향과 객체 지향 프로그래밍

- 절차지향 프로그래밍 (step by step) / 냉장고에 코끼리를 넣는다
1. 냉장고 문을 연다. -> open 냉장고
2. 코끼리를 냉장고에 넣는다. -> insert 코끼리 into 냉장고
3. 냉장고 문을 닫는다. -> close 냉장고

- 객체 지향 프로그래밍
1. 코끼리라는 사물의 기능, 정보에 대한 설계도를 만든다.
2. 이 설계도를 기반으로 코끼리1 객체를 만든다.
3. 냉장고라는 사물의 기능, 정보에 대한 설계도를 만든다.
4. 이 설계도를 기반으로 냉장고1 객체를 만든다.
5. 코끼리1 의 객체의 기능을 호출해서, 냉장고1의 객체의 문을 연다.
6. 코끼리1 의 객체의 기능을 호출해서, 냉장고1의 객체안으로 들어간다.
7. 냉장고1 의 객체의 기능을 호출해서, 냉장고1의 객체의 문을 닫는다.

정리:
1) 해당 사물을 나타낼 수 있는 설계도를 만든다. ( Class )
2) 해당 사물의 설계도를 기반으로 사물1 객체를 만든다. ( Object )
3) 사물1 객체의 기능을 호출한다. ( attribute, method )
    - attribute : 사물1의 객체의 변수
    - method : 사물1 객체의 함수

호출 -> 사물1객체의이름.method이름(인자)
'''
string = "Fun Coding" # 문자열 관련 설계도가 있음 - 해당 설계도 기반 문자열1 객체가 만들어진다.
a = string.split() # 해당 문자열1 객체가 가지고 있는 메서드(method)
print(a)

##########################################################################################
# 예제로 이해하는 객체지향 문법(class 와 object)
# 사각형 만들기
# 1. class 선언하기
'''
class 클래스이름:
    attribute 선언
    method 선언
'''
class Qurd():
    width = 0
    height = 0
    color = ''
    name = 'Qurd'

    def qurd_name(self, argument1, argument2):
        print(argument1, argument2)
        return self.name

# 2. 객체 생성
qurd1 = Qurd()
qurd2 = Qurd()

# 3. 객체 기능 호출
qurd1.width = 10
qurd1.height = 10
qurd1.color = 'blue'
qurd1.name = 'blue qurd'

qurd2.width = 5
qurd2.height = 5
qurd2.color = 'yellow'
qurd2.name = 'yellow qurd'

print(qurd1.width, qurd2.width) # 객체마다 조작해서 변화 가능

print(qurd1.qurd_name(1, 2), qurd2.qurd_name(4, 5))

