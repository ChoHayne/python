from Day15.Model.character_abc import Characters


class Mage(Characters):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.mana = 100

    def attack(self):
        print("지팡이 휘두르기")

    def defend(self):
        print("보호 마법")

    def special(self):
        if self.mana < 10:
            print("마나가 부족합니다")
        else:
            print("마법에너지 공격")
            self.mana -=10