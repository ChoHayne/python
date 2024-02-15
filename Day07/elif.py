#elif
'''
a = -1
if a > 0:
    print("양수입니다.")
elif a == 0:
    print("0입니다.")
else:
    print("음수입니다.")
'''


# 유저에게 영어 점수를 입력받고
# 90점 이상 A, 80이상 B, 70이상 C, 나머지 fail
'''
score = int(input("영어점수를 입력:"))
if score >= 90:
    if score == 100:
        print('excellent!', end=' ')
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('Fail')
'''

#정수를 입력받고, 양의 홀수, 양의 짝수, 0, 음의홀수, 음의짝수
'''
a = int(input("숫자입력:"))
if a > 0:
    if a%2 == 0:
        print('양의 짝수')
    else:
        print('양의 홀수')
elif a == 0:
    print('0')
else:
    if a % 2 == 0:
        print('음의 짝수')
    else:
        print('음의 홀수')
'''
'''
num = int(input("숫자입력:"))
if num > 0:
    if num % 2 == 1:
        print("양의 홀수")
    else:
        print("양의 짝수")
elif num == 0:
    print("0")
else:
    if num % 2 ==1:
        print("음의 홀수")
    else:
        print("음의 짝수")
'''

# 비밀번호 설정 프로그램
# 유저에게 비밀번호 설정을 입력받고, 아래 조건이 성립되도록 프로그램
#1. 최소 10글자 이상 -> 틀리면 10글자 이상이어야 합니다.
#2. !,@,#이 하나라도 포함해야함. -> 틀리면 !,@,# 중 꼭 포함!
#3. 첫번째 글자가 무조건 대문자 -> 틀리면 첫번째 문자가 반드시 대문자.
#4. 위 사항을 모두 통과하면 비밀번호 설정완료!

'''
password = input("비밀번호를 입력하세요:")
if len(password) <10:
    print("10글자 이상이어야 합니다.")
else:
    if '!' in password:
        if password[0].islower():
            print("첫번째 문자가 꼭 대문자야여합니다.")
        else:
            print("비밀번호 설정완료!")
    elif '@' in password:
        if password[0].islower():
            print("첫번째 문자가 꼭 대문자야여합니다.")
        else:
            print("비밀번호 설정완료!")
    elif '#' in password:
        if password[0].islower():
            print("첫번째 문자가 꼭 대문자야여합니다.")
        else:
            print("비밀번호 설정완료!")
    else:
        print("'!','@','#'가 반드시 포함되어야 합니다.")
'''
'''
password = input("비밀번호 설정:")
if len(password) <10:
    print("10글자보다 적음")
elif not ('!' in password or '@' in password or '#' in password):
        print("'!','@','#'가 반드시 포함되어야 합니다.")
        #세 조건이 전부 다 True가 아닐때
        # 0, [], False를 제외하면 모두다 true
        # if는 boolean을 판단함.
elif password[0].islower():
    print("첫번째 문자가 꼭 대문자야여합니다.")
else:
    print("비밀번호 설정완료!")
    
'''
'''
password = input("비밀번호 설정:")
if password[0].islower() or len(password)<10:
    print("비밀번호는 10글자 이상, 첫 글자는 대문자")
else:
    if '!' in password or '@' in password or '#' in password:
         print("비밀번호 설정완료!")
    else:
        print("'!','@','#'가 반드시 포함되어야 합니다.")
'''
###
'''
#버스요금 계산기
1:시내버스-1200원
2:광역버스-2000원
3:마을버스-1000원
연령별 할인율
어린이 7세이하 무료
청소년8~19세 30%할인
노인(65세이상) 무료

나이와 노선에 따라 최종 버스요금
'''
'''
fare = {
     '시내버스' : 1200,
     '광역버스' : 2000,
     '마을버스' : 1000
    }

bus = input("무슨버스타세요? 시내버스, 광역버스, 마을버스:")
age = int(input("몇살이신가요:"))
if age <= 7 or age >= 65:
    print("무료입니다.")
elif age >= 8 and age <= 19:
    print(f"당신의 버스요금은 {(fare[bus]*0.7)}입니다.")
else:
    print(f"당신의 버스요금은 {fare[bus]}입니다.")
'''

bus = {
    'type' : ['시내버스', '광역버스', '마을버스'],
    'price' : [1200,2000,1000]
}

choice = int(input(f"{bus['type']}에서 고르세요 (0~2번):"))
age = int(input("나이 입력:"))

if age <= 7 or age >= 65:
    print("무료입니다.")
elif 8 <= age <= 19:
    print(f"{(bus['price'][choice])*0.7}원입니다.")
else:
    print(f"{(bus['price'][choice])}원입니다.")