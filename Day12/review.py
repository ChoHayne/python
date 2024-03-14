#1 정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서 k의 배수를 오름 차순으로 저장한 배열을 return하는 solution함수를 완성해 주세요.


"""
def solution:                 # 매개변수 빼먹었쥬 그래서 돌아갔쥬
    n = int(input("정수 n 값을 입력하시오. :"))
    k = int(input("정수 k 값을 입력하시오. :"))
    for k in range(1:n+1):
        for i in range(:k):
        다까먹었누
"""

def solution1(n,k):
    return [(i + 1) * k for i in range(n // k)]

print(solution1(10,3))


#2 저번에 했음 arr, k

def solution2(arr,k):
 """
   if k % 2 ==1:
        return [ i*k for i in arr ]
    else:
        return [ i+k for i in arr ]
 """
 return [ i*k if k % 2 ==1 else i + k for i in arr]


#3 주어진 문자열 리스트를 하나의 문자열로 병합하는 함수를 reduce를 사용하여 작성하시오. 각문자열 사이에는 공백을 넣으세요
# 예시입력: ['python', 'is', 'awesome!'] ---> 예시출력: 'python is awesome!'

from functools import reduce
"""
print(reduce(lambda x,y: x+' '+y,['python', 'is', 'awesome!']))
"""
wordList = ['python', 'is', 'awesome!']
def concat(acc,cur):
    return acc + ' ' + cur
res = reduce(concat, wordList)
print(res)

#4 주어진 숫자 리스트에서 짝수인 요소의 개수를 세는 함수를 reduce를 사용하여 작성하시오.
# 예시입력: [1,2,3,4,5,6] ---> 예시출력: 3

numList = [1,2,3,4,5,6]
def countEven(acc,cur): #cur = current, acc=accumulation
    if cur % 2 == 0:
        return acc+1
    else:
        return acc

res1 = reduce(countEven, numList, 0) #0은 acc 의 초기값 안넣으면 list의 제일 처음 값을 acc 초기 값으로 잡음.
print(res1)