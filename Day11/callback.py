#callback 함수 [합성 함수]

# f(x) = x + 5 ; f(1) = 6
# f(g(x)) [합성함수] : 유연해짐 <=> 노가다를 줄여줌.

def test(x): #x에 함수를 넣어보자
    print("함수 시작")
    x()
    #x() 이거 자체가 함수 그래서 이자리에 들어가는 함수가 실행되는거임
    #아래 함수가 return 1이면 """TypeError: 'int' object is not callable"""
    #x() 는 "함수를 실행해"라는 명령어
    print("함수 끝")

def make_fry(): #매개 변수가 안필요한 함수라서 () 비어있음.
    print("🍳")
"""
test(make_fry) #함수를 넣는것

# test(make_fry()) #make_fry() -> return 값 -> None 오 이해함 think of when def make_fry() .... return 1 then its result would be 1

def make_rice():
    print("🍚")

def make_noodle():
    print("🍜")

def make_taco():
    print("🌮")
"""

# pick_fruit(x):
# res = x() ["🍎","🍋","🍒"]
# print("{res}과일을 얻었습니다.") 하는 함수를 정의

def pick_fruit(x):
    res = x()
    print(f"{res} 과일을 얻었습니다.")
"""
def apple():
    return "🍎"

def lemon():
    return "🍋"

def cherry():
    return "🍒"
"""

a = lambda : "🍎"
b = lambda : "🍋"
c = lambda : "🍒"

pick_fruit(a)