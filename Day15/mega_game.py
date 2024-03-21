from Day15.Model.archer import Archer
from Day15.Model.mage import Mage
from Day15.Model.warrior import Worrior

print("메가 게임")

character_number = input("캐릭터를 선택하세요 1. 전사 2. 마법사 3. 궁수")
name = input("이름을 입력하세요")
choice = {
    "1": Worrior(name, 200),
    "2": Mage(name,100),
    "3": Archer(name,150)
}
character = choice[character_number]

while True:
    selected = input("1. 공격하기 2.방어하기 3.특수능력")
    if selected == "1":
        character.attack()
    elif selected == "2":
        character.defend()
    elif selected == "3":
        character.special()
    else:
        print("해당 번호는 없습니다.")

# 이걸 다같이 하는게 게임서버