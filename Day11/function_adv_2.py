# 함수 정의 하는 법
def add(x,y):
    return x+y
def makeApple(x):
    return ['🍒' for i in range(x)]

# 함수 정의 하는 방법 with 매개 변수 n개 일 때
# 매개변수에 *를 붙이면 n개로 대체..................대체왜?
def make_pizza(*toppings): # toppings 는 range 같은 역할이 됨
    for i in toppings:
        print(f"추가 토핑: {i}")

make_pizza("치즈","파인애플","불고기","페퍼로니","올리브")

# make_upper(words)
# 소문자로 매개변수 들어오면
# 대문자로 출력해주는 함수

def make_upper(*words):
    for i in words:
        print(i.upper())

# i 는 iterate 되는 list 안의 '내용물'

make_upper("kakao","cheese","cake")


# 숫자가 홀수면 홀수입니다, 짝수면 짝수입니다 라고 말하는 함수
def oddoreven(*numbers):
    for i in numbers:
        if i % 2 == 1:
            print(f"{i}는 홀수입니다.")
        else:
            print(f"{i}는 짝수입니다.")

oddoreven(1,2,3,9,11,1134)



