#dict: key[중복안됨, int, str] - value[중복 가능, any type]

'''
coffee = {
    1:"아메리카노",
    2:"라떼",
    3:"바닐라",
}

# 이때 1,2,3이 key, "~"가 value에 해당

cgv = {
    'A':'웡카',
    'B':'시민덕희',
    'C':'귀멸의칼날'
}
print(coffee[3])
print(cgv['C'])
'''

#mini quiz_mbti
#유저에게 mbti 입력받고 유저의 mbti성향을 알려주는 프로그램 만들기
# entj = 외향적이고 xxx이고 xxxx이며 xxx이군요.
mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'현실적',
    'n':'공상적',
    't':'이성적',
    'f':'감정적',
    'p':'즉흥적',
    'j':'계획적'
    }

'''
userMbti = input("mbti를 입력하세요:")
mbtiElements = list(userMbti)
print(mbti[{mbtiElements}])

mbti[''] ##[>>''<<]이게 안필요함

'''
'''
userMbti = input("mbti가 뭐니:")
print(userMbti[0])
print(f"당신의 유형은 { mbti[ userMbti[0] ] } {mbti[userMbti[1]]} {mbti[userMbti[2]]} {mbti[userMbti[3]]} 이군요")
'''

