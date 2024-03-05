#lambda(=익명함수)
def add(x,y):
    return x+y


# lambda x,y: x+y
#lambda x,y: x*y
"""
a = 123
b = "123"
c = ['아아','라떼','바닐라']
d = lambda x,y: x+y #<-이제 변수에 함수를 넣을 수 있어!OH
"""


a = lambda x,y : x+y
b = lambda x,y : x*y
c = lambda x: x.upper()
res = a(3,15) #18
res1 = b(1,5) #5
res2 = c("power")
print(res2)