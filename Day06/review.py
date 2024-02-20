'''
1. 유저에게 설날먹은 음식3개 묻고 설날먹은 음식리스트로

2. 유저에게 좋아하는 커피 프랜차이즈 영어로 입력받고 대문자화

3. 유저에게 이메일 주소를 입력받고 도메인만 출력하기
ex) megastudy@naver.com -> naver
'''


'''
print(), input(), int(), str(), bool()
"abcdef".upper() << 어떻게 하겠다의 모임.
'''
'''
b= [1,2,3,4,5]
b.append(100)
print(b)
'''
'''
#1

sulFood = []
k1 = input("설날에 먹은 음식:")
k2 = input("설날에 먹은 음식:")
k3 = input("설날에 먹은 음식:")
sulFood.append(k1)
sulFood.append(k2)
sulFood.append(k3)
print(f"설날에 먹은음식리스트:{sulFood}")
'''
'''
#2
coffee = input("좋아하는 커피 프차: ")
print(coffee.upper())
'''
'''
a = "hellow!world".split("!")
print(a)
'''
#3. split 이용 .split("기준")
#a@naver.com
'''
domain = input("메일주소:")
m1 = domain.split("@")
m2 = m1[1].split(".")
print(m2[0])
'''

'''
print(wordList)
'''

'''
#4 영어 기사를 스크랩하여서 단어별로 리스트화 해서 오름차순으로 출력하기
article = """The government-run Kyiv Scientific Research Institute of Forensic Expertise said in a Telegram post that debris recovered after a February 7 attack on the Ukrainian capital pointed to the use of a Zircon hypersonic cruise missile by the Russian military.

“Markings on the parts and fragments, the identification of components and parts, and the features of the relevant type of weapon” point to the first-ever use of the Zircon in combat, said the institute, which is part of Ukraine’s Justice Ministry."""
wordList = article.split(" ")
wordList.sort()
'''
