# import random

# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[0]
#     left = [num for num in arr[1:] if num < pivot]
#     right = [num for num in arr[1:] if num >= pivot]
#     arr = quick_sort(left) + [pivot] + quick_sort(right)
#     return arr

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

# testCase1 = [7, 5, 4, 1, 6]
# testCase2 = [1, 1, 1, 0, 0, 0]
# testCase3 = [random.randint(0, 100) for i in range(20)]
# print(quick_sort(testCase1))
# print(quick_sort(testCase2))
# print(quick_sort(testCase3))