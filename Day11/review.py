# 1. 조건에 맞게 수열 변환하기
"""
정수배열 arr와 자연수 k가 주어집니다. 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
k가 짝수라면 arr의 모든 원소에 k를 더합니다. 이러한 변환을 마친 후의 arr를 return하는
solution 함수를 완성해주세요
arr                     k           result
[1,2,3,100,99,98]       3           [3,6,9,300,297,294]
[1,2,3,100,99,98]       2           [3,4,5,102,101,100]
"""
"""
arr = [1,2,3,100,99,98]
k_val = int(input("k값을 입력하세요"))
if k_val % 2 == 1:
    for i in len(arr):
        arr[i] = arr[i] * k_val
        print(arr)
else:
    for i in arr:
        arr[i] = arr[i] + k_val
        break
print(arr)

"""

"""

def solution(arr,k):
    if k % 2 == 1:
        newList = []
        for i in arr:
            newList.append(i*k)
        return newList # 함수를 알려줌
    else:
        newList = []
        for i in arr:
            newList.append(i+k)
        return newList


# 단축버전
def solution(arr,k):
    if k % 2 == 1:
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]

# 더단축
def solution(arr,k):
    return [ i * k if k % 2 == 1 else i + k for i in arr]

"""

# 제일 작은 수 제거하기
"""
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수,
solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
예를 들어, arr 이 [4,3,2,1]인 경우는 [4,3,2]를 리턴하고, [10]이면 [-1]을 리턴합니다.
"""

"""
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
    return arr

"""


def removeMinArr(arr):
    if len(arr) == 1:
        return [-1]
    else:
        # arr.sort()
        # len, sum(리스트를 넣었을 때 합을 알려줌), max(리스트안의 가장큰애), min(리스트 안의 가장 작은애)
        minimum = min(arr)
        arr.remove(minimum)
        return arr
