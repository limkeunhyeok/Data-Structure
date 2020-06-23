# import random

def bubble_sort(arr):
    arrLength = len(arr)
    for i in range(arrLength):
        for j in range(arrLength - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(bubble_sort(testCase1))
# print(bubble_sort(testCase2))
# print(bubble_sort(testCase3))