#lexical(=어휘)

mega = "ice" # global variable(전역 변수)

def abc():
    mega = "123"
    # mega 라는 변수는 abc() 라는 함수에 갇혀있음.(=local variable; 지역 변수)
    # 그리고 여기서 쓰인 변수는 잊혀짐(->메모리 아낄수있음)
    return mega

a = abc()
print(a)
print(mega)

def xyz():
    print(mega)

xyz()