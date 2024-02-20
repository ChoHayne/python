#for_comp:for_comprehension : for문 간결한 버전
'''
for i in range(10):
'''

#List for_comprehension
'''
newList = [i for i in range(100)]
print(newList)
appleList = ['🍎' for i in range(100)]
print(appleList)
'''
#25~75
'''
numRangeList = [i for i in range(25,76)]
print(numRangeList)
'''

# fruits = ['🍎','🍒','🍋']
'''
fruitList = [i*('🍎','🍒','🍋') for i in range(10)]
'''
'''
fruitList = [fruits[i%3] for i in range(100)]
print(fruitList)
'''
'''
helloworldList = [i.upper() for i in "hello world"]
print(helloworldList)
'''

coffee = ['americano','latte','mint','mocha','cocoa']
coffeeLen = [len(i) for i in coffee]
print(coffeeLen)
