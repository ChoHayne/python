from Day15.Model.character_abc import Characters


class Archer(Characters):
    def __init__(self,name, health):
        super().__init__(name,health)
        self.arrows = 50

    def attack(self):
        print("화살 날리기")
        self.arrows -= 1

    def defend(self):
        print("회피")

    def special(self):
        print("화살통 채우기")
        self.arrows = 50