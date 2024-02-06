'''

#1

a = int(input("나이 입력하시오: "))
print("나이가 %d이면 출생년도는 %d입니다." %(a,2025-a))

#2

b = float(input("한 변의 길이(cm)를 입력하시오:"))
print("한 변의 길이가 %dcm이면, 넓이는 %dcm2입니다." %(b,b**2))

'''

# f"" 이거써라

'''
#1번퀴즈
age = int(input("몇살이냐?:"))
print(f"나이가 {age}살이면, 출생년도는 {2025 - age}년입니다.")

#2번퀴즈
side = int(input("한변의길이:"))
print(f"한변의 길이가{side}cm이면, 넓이는 {side**2}cm^2 입니다.")

#3번 퀴즈 밑변과 높이
length = int(input("밑변의 길이:")) #밑변을 base라고 해?
height = int(input("높이의 길이:"))
print(f"삼각형의 넓이는 {length*height*0.5}")

'''

'''
#4
c = input("10000부터 99999사이의 정수를 입력하시오: ")
print(f"{c[0]}만{c[1]}천{c[2]}백{c[3]}십{c[4]}")

#5
d = int(input("초단위로 숫자를 입력하시오"))
e = d%3600
f = e%60
print(f"{d//3600}:{e//60}:{f}")

#6
g = input("10000부터 99999사이의 정수:")
h = int(g[2])
print(f"{h*100}")

'''

num = int(input("10000~99999 사이 정수 입력:"))
ten_thousands = num//10000
thousands = (num % 10000)//1000
hundreds = (num % 1000)//100
tens = (num % 100)//10
one = num % 10
print(f"{ten_thousands}만{thousands}천{hundreds}백{tens}십{one}")