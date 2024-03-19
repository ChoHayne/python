"""
class Minion:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

class MeleeMinion(Minion): #(Minion) <- 상속을 받았다.
    def __init__(self,hp,attack,distance):

"""


class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand,horsePower):
        super().__init__(brand) #super() <- 부모
        self.horsePower = horsePower

class Airplane(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model



class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print("호흡중")


class Dog(Animal):
    def __init__(self, name, master):
        super().__init__(name)
        self.master = master

    def bark(self):
        print("멍멍")

class Rooster(Animal):
    def __init__(self, name, comb):
        super().__init__(name)
        self.comb = comb

    def crow(self):
        print("꼬꼬댁")


bori = Dog("보리","성희")
dark = Rooster("달이","빨간색")

bori.bark()
dark.crow()
bori.breath()
dark.breath()


# 상속 (Inherence)
## 코드의 재사용성, 프로그램 구조 효율성

"""
class ParentClass:
    pass

class ChildClass(ParentClass):
    # 자식 클래스에서 추가된 메서드와 속성 정의
    pass
"""