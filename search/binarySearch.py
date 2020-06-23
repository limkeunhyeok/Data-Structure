import random

def binary_search(num):
    start = 0
    end = 100000
    while True:
        mid = (start + end) // 2
        if mid == num:
            return mid
        elif mid > num:
            end = mid - 1
        else:
            start = mid + 1

print('random 변수 생성!')
n = random.randint(0, 100000)
print('random 변수: ', binary_search(n))