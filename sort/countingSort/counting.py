# import random

def counting_sort(arr, K):
    c = [0] * K
    sortedArr = [0] * len(arr)

    for i in arr:
        c[i] += 1

    for i in range(1, K):
        c[i] += c[i - 1]

    for i in range(len(arr)):
        sortedArr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return sortedArr

# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(counting_sort(testCase1, 10))
# print(counting_sort(testCase2, 2))
# print(counting_sort(testCase3, 100))