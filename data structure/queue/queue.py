class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    
    def dequeue(self):
        if self.front is None:
            return 'empty'
        else:
            dequeueNode = self.front
            self.front = self.front.next
            return dequeueNode.data

    def peek(self):
        if self.front is None:
            return 'empty'
        else:
            return self.front.data
    
    def size(self):
        if self.front is None:
            return 0
        else:
            current = self.front
            count = 1
            while current is not self.rear:
                current = current.next
                count += 1
            return count

    def show(self):
        if self.front is None:
            return 'empty'
        else:
            current = self.front
            string = ''
            while current.next is not None:
                string += str(current.data) + '->'
                current = current.next
            string += str(current.data) + '->'
            return string

q = Queue()
print('size: ', q.size()) # 0
print('dequeue: ', q.dequeue()) # empty
print('peek: ', q.peek()) # empty
q.enqueue(1)
print('front: ', q.front.data) # 1
print('rear: ', q.rear.data) # 1
q.enqueue(2)
q.enqueue(3)
print('front: ', q.front.data) # 1
print('rear: ', q.rear.data) # 3
print('size: ', q.size()) # 3
print('peek: ', q.peek()) # 1
print('dequeue: ', q.dequeue()) # 1
q.enqueue(4)
q.enqueue(5)
print('size: ', q.size()) # 4
print('show: ', q.show()) # 2->3->4->5->
print('front: ', q.front.data) # 2
print('rear: ', q.rear.data) # 5
q.dequeue()
q.dequeue()
q.dequeue()
print('peek: ', q.peek()) # 5
print('dequeue: ', q.dequeue()) # 5
print('dequeue: ', q.dequeue()) # empty