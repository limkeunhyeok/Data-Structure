import sys
from random import randint
from time import time
from bubbleSort.bubble import bubble_sort
from selectionSort.select import selection_sort
from insertionSort.insert import insertion_sort
from mergeSort.merge import merge_sort
from quickSort.quick import quick_sort
from countingSort.counting import counting_sort

sys.setrecursionlimit(10**7)

testCase = [randint(0, 20000) for i in range(10000)]
sortType = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]

def parse(sort):
    return str(sort).split(' ')[1]

for sort in sortType:
    start = time()
    sort(testCase)
    end = time()
    print(parse(sort), ': ', end - start)

start = time()
counting_sort(testCase, 20000)
end = time()
print('counting_sort : ', end - start)