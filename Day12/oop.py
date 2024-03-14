# 절차지향 : Procedural Programming(PP) 위에서 아래로, 순차적으로, 작은 규모에 적합; 절차지향 프로그밍은 컴퓨터 프로그래밍의 가장 기초적인 형태 중 하나로, 주어진 문제를 해결하기 위한 연산의 순서와 흐름을 정의합니다. 이 접근 방식에서는 프로그램을 작업을 수행하는 순서에 따라 조직화하며, 이는 알고리즘의 시행 경로를 명확하게 표현하는데 유리합니다.
## 핵심요소: 함수, 순서, 조건, 반복 --->단순성, 순차적 접근
# 객체지향 : Object-Oriented Programming(OOP), 대규모 = 하루안에 못만듦;


# 변수 -> 데이터 타입
# 정수 타입, 실수 타입, 문자열 타입 => 나만의 타입
# 변수 모음[(명사)학번,id,학과,이름] + 함수 모음[(동사)학점입력,이름바꾸기,전과하기] = 대학생[Object]

# class의 격은 if, while 이랑 동일
class Student: #Student라는 "새로운 변수'타입'"(=object)을 만듦
    # 예시 변수모음(이름,학과) + 함수모음(과바꾸기) = 학생
    # 활용 template 뼈대 역할
    # 프로그램의 목표가 정해지고 class를 만듦.

    # 속성[데이터]
    def __init__(self,a,b):
        self.name = a
        self.age = b

    # 함수[메서드]
    def getAge(self):
        self.age += 1

a = Student("김민규",11)
b = Student("박관영",13)
#이때 a,b는 instance
print(a.age)
b.getAge()
print(b.age)

# 객체의 개념
## 객체란: 객체는 속성(변수)과 메서드(함수)를 하나의 단위로 묶은 것입니다.
### 속성(Attributes) : 속성은 객체의 특징. 예) 자동차 ->색상, 브랜드, 연식 등
### 메서드(Methods) : 객체가 수행할 수 있는 행동. 예) 자동차 ->운전하기, 정지하기, 경적울리기 등.

# 클래스 : '틀'or'모형' 예) 고양이 클래스 -> 샴고양이, 코리안숏, ...
##1. 클래스구조: class 키워드를 사용하고 클래스의 이름을 적어줌. """이름의 첫 글자는 >>대문자<<로 적는 것이 관례."""
##### pass 는 아무것도 실행하지 않고 일단 클래스를 만들게.
##2. __init__ 메서드와 초기화: __init__ 자체가 ""함수"". 객체의 초기 상태를 설정하는데 사용.
##3. 클래스 이름 짓기: 보통 명사로 지음. 명사+명사 일 경우 대문자시작대문자시작 조합으로 만드는 것이 관례. 예) MyClass, WifiInformation, ...

# 클래스 기본 구조
##1. 클래스 선언
##2. 속성
##3. 메서드
##4. 생성자(init 메서드)
##5. self키워드: self는 클래스의 인스턴스 자신을 참조하는 변수입니다. 메서드 내에서 클래스의 속성이나 다른 메서드에 접근할 때 사용됩니다.



# car: company, model, year // honk()--"빵빵"이라고 함, intro(attributes를 소개)

class Car:
    def __init__(self,a,b,c):
        self.company = a
        self.model = b
        self.year = c

    def honk(self):
        print("빵빵") # 이 친구는 print를 했지만 본인은 none

    def intro(self):
        print(f"이 차는 {self.company}에서 {self.year}년에 제작된 {self.model}입니다.")

    def honk1(self):
        return "빵빵" # print를 해야 보여줌

carA = Car("현대","스포티지",2020)
carA.intro()
carA.honk()
carB = Car("기아","베뉴",2018)
carB.intro()