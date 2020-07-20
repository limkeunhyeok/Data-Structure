class Node:
    def __init__(self, data):
        self.data = data
        self.frontLink = None
        self.rearLink = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def push_front(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = newNode
            self.front.rearLink = self.rear
            self.rear = newNode
            self.rear.frontLink = self.front
        else:
            self.front.frontLink = newNode
            newNode.rearLink = self.front
            self.front = newNode

    def push_rear(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = newNode
            self.front.rearLink = self.rear
            self.rear = newNode
            self.rear.frontLink = self.front
        else:
            self.rear.rearLink = newNode
            newNode.frontLink = self.rear
            self.rear = newNode
    
    def pop_front(self):
        if self.front is None:
            return 'empty'
        else:
            popNode = self.front
            self.front = self.front.rearLink
            self.front.frontLink = popNode.frontLink
            return popNode.data
    
    def pop_rear(self):
        if self.rear is None:
            return 'empty'
        else:
            popNode = self.rear
            self.rear = self.rear.frontLink
            self.rear.rearLink = popNode.rearLink
            return popNode.data

    def show(self):
        if self.front is None:
            return 'empty'
        else:
            current = self.front
            string = ''
            while current.rearLink is not None:
                string += str(current.data) + '->'
                current = current.rearLink
            string += str(current.data) + '->'
            return string


dq = Deque()
dq.push_front(1)
dq.push_rear(2)
dq.push_front(3)
dq.push_rear(4)
print(dq.show()) # 3->1->2->4->
dq.push_front(5)
dq.push_rear(6)
dq.push_rear(7)
dq.push_rear(8)
print(dq.show()) # 5->3->1->2->4->6->7->8
print(dq.pop_front()) # 5
print(dq.show()) # 3->1->2->4->6->7->8
print(dq.pop_rear()) # 8
print(dq.show()) # 3->1->2->4->6->7->