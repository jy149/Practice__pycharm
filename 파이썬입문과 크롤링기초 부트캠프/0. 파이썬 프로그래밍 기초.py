# 파이썬 기본
# 입력과 출력(input, print)
article = '''
t concludes the new variant increases the Reproduction or R number by between 0.4 and 0.7.

The UK's latest R number has been estimated at between 1.1 and 1.3. It needs to be below 1.0 for the number of cases to start falling.

Prof Axel Gandy of London's Imperial College said the differences between the viruses types was "quite extreme".

"There is a huge difference in how easily the variant virus spreads," he told BBC News. "This is the most serious change in the virus since the epidemic began," he added.

The Imperial College study suggests transmission of the new variant tripled during England's November lockdown while the previous version was reduced by a third.

Cases of Covid-19 have begun to increase rapidly during the second spike, and the number of cases recorded in a single day reached a new high on Thursday.
'''
print(article.count('new'))
print(len(article)) # 띄어쓰기도 포함하는거다, 다음 row로 넘어가는 \n 도 표현하는거.
print(article.find("new"))
#print(article.replace("London", "Korea")) # 특정 문자열 변경
print(article[-2])
print()
################################################

string1 = 'python'
print(string1)
some_string = "    computer    "
print(some_string, len(some_string))
print(some_string.strip(), len(some_string.strip()))
print()
################################################
# 다양한 출력
print("I have a {}, I have an {}.".format("pen", "apple"))
print("I have a {1}, I have an {0}.".format("pen", "apple"))
print("I have a {0}, I have an {0}.".format("pen", "apple"))
print()
###
interest = 0.08751
print(format(interest, ".2f"))
print(format(interest, ".3f"))
###
print("I have a %d, I have an %s." % (1,"apple"))
print()

