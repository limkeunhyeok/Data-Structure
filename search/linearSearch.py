import random

def linear_search(num):
    i = 0
    while True:
        if i == num:
            return i
        else:
            i += 1

print('random 변수 생성!')
n = random.randint(0, 100000)
print('random 변수: ', linear_search(n))