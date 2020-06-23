# import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        leftArr = merge_sort(left)
        rightArr = merge_sort(right)
        return merge(leftArr, rightArr)
    else:
        return arr

def merge(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    
    while i < len(left):
        arr.append(left[i])
        i += 1
    
    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr



# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(merge_sort(testCase1))
# print(merge_sort(testCase2))
# print(merge_sort(testCase3))