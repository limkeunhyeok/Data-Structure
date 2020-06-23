# import random

def insertion_sort(arr):
    arrLength = len(arr)
    for i in range(1, arrLength):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(insertion_sort(testCase1))
# print(insertion_sort(testCase2))
# print(insertion_sort(testCase3))