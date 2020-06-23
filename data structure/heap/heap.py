class MaxHeap:
    def __init__(self):
        self.arr = []

    def swap(self, index, parentIndex):
        self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]

    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return index * 2 + 1
    
    def right_child(self, index):
        return index * 2 + 2

    def insert(self, data):
        self.arr.append(data)
        index = len(self.arr) - 1
        while 0 <= index:
            parent_index = self.parent(index)
            if parent_index >= 0 and self.arr[parent_index] < self.arr[index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def delete(self):
        index = len(self.arr) - 1
        if index < 0:
            return 'empty'
        self.swap(0, index)
        data = self.arr.pop()
        self.maxHeapify(0)
        return data

    def maxHeapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        maxIndex = index

        if left <= len(self.arr) - 1 and self.arr[maxIndex] < self.arr[left]:
            maxIndex = left
        if right <= len(self.arr) - 1 and self.arr[maxIndex] < self.arr[right]:
            maxIndex = right

        if maxIndex != index:
            self.swap(index, maxIndex)
            self.maxHeapify(maxIndex)

    def show(self):
        string = ''
        for num in self.arr:
            string += str(num) + ' '
        print(string)

h = MaxHeap()
h.insert(3)
h.insert(1)
h.insert(4)
h.insert(7)
h.insert(6)
h.insert(11)
h.insert(5)
h.show() # 11 6 7 1 4 3 5
h.delete()
h.show() # 7 6 5 1 4 3
h.delete()
h.show() # 6 4 5 1 3