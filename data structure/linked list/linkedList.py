class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            current = self.head            
            while current.next is not None:
                current = current.next
            current.next = newNode

    def delete(self):
        if self.head is None:
            return 'empty'
        elif self.size() == 1:
            deleteData = self.head
            self.head = None
            return deleteData.data
        else:
            current = self.head
            previous = current
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            return current.data

    def size(self):
        if self.head is None:
            return 0
        else:
            current = self.head
            count = 1
            while current.next is not None:
                current = current.next
                count += 1
            return count

    def show(self):
        if self.head is None:
            return 'empty'
        else:
            string = ''
            current = self.head
            while current.next is not None:
                string += str(current.data) + '->'
                current = current.next
            string += str(current.data) + '->'
            return string

l = LinkedList()
print('size: ', l.size()) # 0
print('delete: ', l.delete()) # empty
print('show: ', l.show()) # empty
l.append(3)
l.append(4)
l.append(1)
l.append(2)
print('size: ', l.size()) # 4
print('delete: ', l.delete()) # 2
print('delete: ', l.delete()) # 1
l.append(6)
l.append(1)
l.append(8)
print('size: ', l.size()) # 5
print('show: ', l.show()) # 3->4->6->1->8->
l.delete()
l.delete()
l.delete()
l.delete()
print('delete: ', l.delete()) # 3
print('delete: ', l.delete()) # empty