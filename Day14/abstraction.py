from abc import ABC, abstractmethod


# Shape 클래스를 만들었는데 뭐라고 구체적으로는 못하지만 area랑 round라는 메소드를 꼭 갖고있어야해
# 추상 클래스는 미리 자식들이 가질 속성과 메소드를 규격화.

class Shape(ABC): #?? Shape라는 class는 area랑 round(둘레)라는 함수를 갖고 있단다. 라고 선언만 해줌.
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def round(self):
        pass
##Shape 클래스 자체가 추상클래스이기때문에 (ABC) 안에 다음과 같은 구체적인 명령이들어가면안됨.

    """
    def calArea(self):
        print(f"{self.area}")

    def calRound(self):
        print(f"{self.round}")
    
    """

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    def round(self):
        return 3.14 * self.radius * 2


# triangle, square 클래스만들고
# circle triangle, square 각각 인스턴스 만들고 각각 넓이와 둘레 출력.
class Triangle(Shape):
    def __init__(self,base):
        self.base = base


    def area(self):
        return 0.87 * 0.5 * self.base ** 2

    def round(self):
        self.round = 3* self.base

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2

    def round(self):
        return 4 * self.side

squ1 = Square(3)
tri1 = Triangle(6)
circle1 = Circle(4)

print(f"{tri1.area}, {tri1.round}")
print(f"{squ1.area}, {squ1.round}")
print(f"{circle1.area}, {circle1.round}")

# 왜 난안되지

# 추상클래스는 '틀', '규칙'만 제공 직접적으로 객체를 생성할 수 없는 클래스 오직 상속용
## 특징
### 1. 인스턴스 생성불가 : 항상 다른 클래스로 얘를 상속받아서 써야됨
### 2. 추상 메소드를 포함: 하나이상의 추상메소드를 포함할 수 있음. 선언만 되어있고 구현은 없음.
### 3. 상속을 위한 기본 틀: 예, round, area 만들기만하고 바로 pass.

## 오버라이딩(Overriding) : 메소드를 자식에서 재정의해서 커스터마이징.