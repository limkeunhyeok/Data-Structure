# import random

def selection_sort(arr):
    arrLength = len(arr)
    for i in range(arrLength):
        minIndex = i
        for j in range(i, arrLength):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(selection_sort(testCase1))
# print(selection_sort(testCase2))
# print(selection_sort(testCase3))