#data_structure

# [](list), {}(set), {}(dict), ()(tuple)

#set(집합, ***중복 허용 안됨***)

'''
a = {1,2,3,1,2,3}
a.add(10)

b = set([1,2,3,4,5,1,2,3,4,5])
print(a)
print(b)
'''
'''
starbucks = ["아메리카노", "라떼", "오늘의커피", "아이스 커피"]
megacoffee = ["아메리카노", "라떼", "딸기라떼", "메가리카노"]
a = set(starbucks)
b = set(megacoffee)
#모든 메뉴가 중복없이 나타나도록 출력
# c = a.union(b)
a.update(b)
print(a)
'''


'''

article1 = """The government-run Kyiv Scientific Research Institute of Forensic Expertise said in a Telegram post that debris recovered after a February 7 attack on the Ukrainian capital pointed to the use of a Zircon hypersonic cruise missile by the Russian military.

“Markings on the parts and fragments."""
wordList = list(set(article.split(" ")))
wordList.sort()
print(wordList)
'''

'''
article1 = """The government-run Kyiv Scientific Research Institute of Forensic Expertise said in a Telegram post that debris recovered after a February 7 attack on the Ukrainian capital pointed to the use of a Zircon hypersonic cruise missile by the Russian military.

“Markings on the parts and fragments."""
article2 = """ the identification of components and parts, and the features of the relevant type of weapon” point to the first-ever use of the Zircon in combat, said the institute, which is part of Ukraine’s Justice Ministry."""

wordList1 = article1.split(" ")
wordList2 = article2.split(" ")
setWL1 = set(wordList1)
setWL2 = set(wordList2)
inter = setWL1.intersection(setWL2)
print(inter)
'''
'''
# 데이터가 추가/삭제되지 않으면 그대로 한줄(=변수 설정 x) ex) .sort()
# 위 사항이 아니면 새로운 변수 넣기

a = [1,2,3,4]
a.sort()
# none으로 돌리냐 마냐의 문제
# cf) intersection
print(a)
input("sdfadf")
'''

