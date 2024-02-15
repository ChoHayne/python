import random
#옵션 아닌 냉장고 같은 느낌

'''
a = random.randint(0,101)
b = random.randint(0,11)
c = ['아메리카노','라떼','바닐라','우유']
print(f"{random.choice(c)}")
print(f"{a} {b}")
'''

#로또번호
#리스트에 6개의 랜덤한 정수(1~45)를 넣어서 보여주기

'''
a = []
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.sort()
print(a)
#중복을 어떻게 없애지?
'''

#유저에게 번호하나를 물어봐서 로또 번호에 있으면 번호 있음 없으면 없음.
a = []
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.append(random.randint(1,45))
a.sort()

userNum = int(input("로또번호 하나만 뽑아봐"))
if userNum in a:
    print("번호 있다")
else:
    print("없다")
print(a)
