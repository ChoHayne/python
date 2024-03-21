# 객체지향 패러다임 SOLID
##1. Single Responsibility Principle (단일 책임 원칙)
###정의: 하나의 클래스, 함수는 하나의 책임만을 가져야 한다. 기능적인 면에서 corresponding하게 이어줌. 포함 되는 영역 잘 분리.

##2. Open-Closed Principle
###정의: 소프트웨어 구성요소(클래스,모듈,함수 등)은 확장에 열려있어야 하며 """수정에는 닫혀있어야함.""" --->일반 명사에 대해 클래스를 설정(확장성) <-> 가장 부모 클래스에는 책임을 부여를 최소화(detail은 상속받아서). =>[확장 지향]

##3. Liskov Substitution Principle(리스코프 치환 원칙)
###정의: 서브클래스(=자식 클래스)는 그것의 기반 클래스(=부모클래스)로 교체될 수 있어야 한다.
###예: 사각형-정사각형 문제; 사각형∋정사각형 => 위반......? 포함되긴 하지만 사각형 클래스에서는 밑변/높이라는 두 변수를 가져야하지만 정사각형은 각각 못함. 그래서 수학적인 개념의 subclassing 보다는 composition같은 다른 방식으로 접근. 개념 <<<<< 프로그램.

##4. Interface Segregation Principle(인터페이스 분리 원칙)
###정의: 클라이언트는 자기가 사용하지않는 메소드에 의존하면 안된다. <-> 레고 처럼 만듦. 완성품이 아니고 조립품st.
###### what if 부모클래스(조류):Method(fly) - 자식클래스(펭귄):못날음 ㅠㅠ <-큰일남.
######### ========> method를 fly 대신 fliable로 뗄 수 있게 바꿈.
#예
#rather than
"""
class Car
def go:
def stop:
def honk:
"""
# it's better
"""
class Car <-Mother class
    class go:
        def goable():
    class stop:
        def breakable():
    class honk:
        def honkable()

class X7 <-child class
    __init__(받을 것들만 받음) <- 유연성 확보
"""

##5. Dependency Inversion Principle(의존성 역전 원칙)
### Top-down method <<<<< Bottom-up method
### 자동차(고수준 모듈)->핸들, 바퀴, 와이퍼,....(저수준 모듈) ===> 핸들,바퀴,와이퍼,... -> 자동차
### 내용물을 먼저 만들고 나서 만드는것이 안정적인 class 설계방법