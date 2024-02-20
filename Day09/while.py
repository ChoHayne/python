# for i in [] start and end vs while unknown



'''
while True:
    num = int(input("숫자0을 입력하면 탈출!"))
    if num == 0:
        break
'''

#더하기 빼기 프로그램
'''
while True:
    print("사칙연산 프로그램")
    num = int(input("1.더하기 2.빼기 3.종료"))
    if num == 1:
        a = int(input("첫 번째 수:"))
        b = int(input("두 번째 수:"))
        print(f"두 수의 합은 {a+b}입니다.")
    elif num == 2:
        a = int(input("첫 번째 수:"))
        b = int(input("두 번째 수:"))
        print(f"두 수의 차는 {a-b}입니다.")
    elif num == 3:
        print("프로그램 종료!")
        break
    elif num == 1004:
        print("사장님 퇴근 요망")
        break
    else:
        print("숫자를 잘못 입력했습니다.")
'''


#도형 넓이 구하는 프로그램
#1. 원의 넓이 2. 정삼각형의 넓이 3. 정사각형의 넓이 4. 프로그램 종료 그외 숫자 재입력 요구
'''
while True:
    print("도형 넓이 구하는 프로그램")
    num = int(input("1. 원의 넓이 2. 정삼각형의 넓이 3. 정사각형의 넓이 4. 프로그램 종료"))
    if num == 1:
        a = int(input("반지름:"))
        print(f"원의 넓이는 {3.14*a**2}입니다.")
    elif num == 2:
        a = int(input("한변의 길이"))
        print(f"정삼각형의 넓이는 {(3**0.5)*(a**2)/4}입니다.")
    elif num == 3:
        a = int(input("한변의 길이"))
        print(f"정사각형의 넓이는 {a ** 2}입니다.")
    elif num == 4:
        print("프로그램 종료!")
        break
    elif num == 1004:
        print("사장님 퇴근 요망")
        break
    else:
        print("숫자를 잘못 입력했습니다.")
'''

# 일본 여행 to-do 리스트
# 0. 여행전 필수 물품 추가하기 1. 갈 곳 등록하기 2. 먹을 것 등록하기 3. 할일 등록하기 4. 모든 to-do list 보기 5. 종료하기
itemList = []
placeList = []
foodList = []
todoList = []

print("일본여행 to-do list")
while True:
    num = int(input("0. 여행전 필수 물품 추가하기 1. 갈 곳 등록하기 2. 먹을 것 등록하기 3. 할일 등록하기 4. 모든 to-do list 보기 5. 종료하기"))
    if num == 0:
        item = input("필수품:")
        itemList.append(item)
        print(f"{item}이 추가되었습니다")
    elif num == 1:
        place = input("갈곳:")
        placeList.append(place)
        print(f"{place}이 추가되었습니다")
    elif num == 2:
        food = input("먹을 것:")
        foodList.append(food)
        print(f"{food}이 추가되었습니다")
    elif num == 3:
        todo = input("할 것:")
        foodList.append(todo)
        print(f"{todo}이 추가되었습니다")
    elif num == 4:
        for i in [itemList,placeList,foodList,todoList]:
            if len(i) == 0:
                print("해당 리스트가 없습니다")
            else:
                print(f"{i}")
    elif num == 5:
        print("종료!")
        #데이터베이스, 엑셀, 핸드폰 저장 장치에 저장하는 코드 넣고 종료
        break
    else:
        print("숫자입력오류!")
