# 프로그램 실행 순서: 위->아래
# 프로그램의 흐름을 제어할 필요할 때가 있다.
# 제어문(control statement): 프로그램의 흐름을 컨트롤함
# -1) 조건문(conditional statement):A이면 B해주세요 eg)if, switch[dict]
# -2) 반복문(loop statement): 여러번 반복해주세요 eg)for, while

# 조건문: if

###
'''
if 조건문:
    실행할 코드
'''
'''
a = int(input("숫자입력:"))

if a > 0:
    print("a는 양수입니다.")
    print("테스팅!")
print("프로그램 끝")
'''

#유저에게 megastudy를 입력하면
#(조건)메가스터디 유저이군요!
#(무조건 나오기) 안녕하세요!
'''
userAffil = input("어디유저세요?")
if userAffil == 'megastudy':
    print("메가스터디 유저시군요!")
print("안녕하세요!")
'''

# 유저에게 영어로 좋아하는 과일을 입력 받고
# apple이면 저도 사과 좋아해요!
# ~~과일은 맛있죠!
'''
userFruit = input("무슨과일을 좋아하는지 영어로쓰세요:")
if userFruit == 'apple':
    print("저도 사과좋아해요!")
else:
    print(f"{userFruit}은/는 맛있죠!")

'''
'''
# if - else
a = int(input("숫자입력:"))
if a > 0:
    print("양수입니다.")
else:
    print("0또는 음수입니다.")
'''

#유저에게 숫자를 입력받고
#홀수인지 짝수인지 판별해주는 프로그램

'''
userInt = int(input("숫자를 입력해주세요:"))
if userInt%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

'''

# 1. 유저에게 영어 단어를 입력받고, 'e'가 있으면 'e' 포함! 없으면 'e' 없음.
# 2. 유저에게 하나의 알파벳을 입력받고, 소문자이면 대문자로, 대문자이면 소문자로 출력.
# 3. 두 숫자를 유저에게 입력받고, 큰 숫자를 출력하는 프로그램.
'''
#1
userAlpha = input("영어단어를 쓰세요:")
if 'e' in userAlpha:
    print("'e'포함!")
else:
    print("'e'없음")
'''
'''
#2.
what: str = input("영어단어를 소문자나 대문자로 입력하세요:")
if what.isupper == True:
    what = what.lower()
else:
    what = what.upper()
print(what)
'''
'''
#3.
a = int(input("첫번째 숫자를 입력하세요:"))
b = int(input("두번째 숫자를 입력하세요:"))
if a > b:
    print(f"둘 중 더 큰 숫자는 {a}")
else:
    print(f"둘 중 더 큰 숫자는 {b}")
'''
'''
word = input("영단어 입력:")
#if 'e' in word:
if word.count('e') > 0:
    print('e 포함!')
else:
    print('e없음!')
'''
'''
alpha = input("알파벳 입력:")
if alpha.islower():
    print(alpha.upper())
else:
    print(alpha.lower())
'''


