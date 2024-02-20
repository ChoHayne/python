#조건부 리스트 for_comprehension
#1. 필터링(거르기) 2.맵핑(바꾸기)

#[i for i in range(n) 조건문]
'''
evenList = [i for i in range(100) if i % 2 == 0]
print(evenList)
'''
words = ['apple','banana','pineapple','mango','kiwi','blueberry','avocado']
'''
longwordsList = [i for i in words if len(i) >= 6]
print(longwordsList)
upperEwordList = [i.upper() for i in words if 'e' in i]
print(upperEwordList)
'''

#2. 맵핑(바꾸기)
#[a if 조건 else b for i in range(n)/list/str]
'''
crush = ['😍' if i % 2 == 0 else i for i in range(100)]
print(crush)
wordsFilter = [i.upper() if len(i) >=5 else i for i in words]
print(wordsFilter)
'''


# 3 6 9 게임
#[1,2,...,100] 3,6,9에서 '👏'

game369 = ['👏' if (i % 10) % 3 or (i//10)%3== 0 else i for i in range(1,101)]

print(game369)
#str으로 처리하는게 맞다. 첫번째 조건때문에
'''
#답
game = ['👏' if str(i%10) in '369' or str(i//10) in '369' else i for i in range(1,101)]
print(game)
'''