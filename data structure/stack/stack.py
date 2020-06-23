class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            return 'empty'
        else:
            popNode = self.top
            self.top = self.top.next
            return popNode.data

    def peek(self):
        if self.top is None:
            return 'empty'
        else:
            return self.top.data
    
    def size(self):
        if self.top is None:
            return 0
        else:
            current = self.top
            count = 1
            while current.next is not None:
                current = current.next
                count += 1
            return count
    
    def show(self):
        if self.top is None:
            return 'empty'
        else:
            string = '->'
            current = self.top
            while current.next is not None:
                string += str(current.data) + '->'
                current = current.next
            string += str(current.data)
            return string

s = Stack()
print('size: ', s.size()) # 0
print('pop: ', s.pop()) # empty
print('peek: ', s.peek()) # empty
s.push(3)
s.push(4)
s.push(1)
s.push(2)
print('size: ', s.size()) # 4
print('top: ', s.top.data) # 2
print('peek: ', s.peek()) # 2
print('pop: ', s.pop()) # 2
print('pop: ', s.pop()) # 1
s.push(6)
s.push(1)
s.push(8)
print('size: ', s.size()) # 5
print('show: ', s.show()) # ->8->1->6->4->3
s.pop()
s.pop()
s.pop()
s.pop()
print('peek: ', s.peek()) # 3
print('pop: ', s.pop()) # 3
print('pop: ', s.pop()) # empty
print('top: ', s.top) # None