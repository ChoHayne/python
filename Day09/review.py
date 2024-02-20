#리스트 요소의 제곱
'''
문제:정수리스트[1,3,5,7,9]의 각요소를 제곱하여 새로운 리스트를 만드세요
예상답:[1,9,25,49,81]
'''
'''
numList = [1,3,5,7,9]
numSqList = []
for x in numList:
    numSqList.append(x**2)
print(numSqList)
'''

numList = [1,3,5,7,9]
numSqList = [i**2 for i in numList]
print(numSqList)

numSqList1 = [i**2 for i in range(1,10,2)] # range로 만듦
print(numSqList1)

#문자열 길이변환
'''
문제:문자열리스트["hello", "world", "python", "programming"]에서 각 단어의 길이를 구하여 새로운 리스트를 만드세요
예상답:[5,5,6,11]
'''
'''
wordList = ["hello", "world", "python", "programming"]
wordList1 = []
for x in wordList:
    wordList1.append(len(x))
print(wordList1)
'''

#문자열 처리를 위한 리스트1
'''
문제: 문자열 리스트["apple","banana","cherry","date"]에서 각 단어의 첫글자만을 추출하여 새로운 리스트를 만드세요
예상답['a','b','c','d']
'''
'''
vocaList = ["apple","banana","cherry","date"]
vocaList1 = []
for x in vocaList:
    vocaList1.append(x[0])
print(vocaList1)
'''
vocaList = ["apple","banana","cherry","date"]
vocaLenList = [len(i) for i in vocaList]
print(vocaLenList)