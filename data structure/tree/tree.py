class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right is None:
                        current.right = newNode
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = newNode
                        break
                    else:
                        current = current.left
    
    def delete(self, data):
        self.root = self.delete_node(self.root, data)
    
    def delete_node(self, node, data):
        if node is None:
            return None
        
        if data == node.data:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                current = node
                while current.left is not None:
                    current = current.left
                node.data = current.data
                node.left = None
                node.right = self.delete_node(node.right, current.data)
                return node
        elif data < node.data:
            node.left = self.delete_node(node.left, data)
            return node
        else:
            node.right = self.delete_node(node.right, data)
            return node

    def show(self, node):
        if node is not None:
            self.show(node.left)
            print(node.data, end=" ")
            self.show(node.right)



t = BST()
t.insert(5)
t.insert(2)
t.insert(3)
t.insert(1)
t.insert(9)
t.insert(8)
t.insert(7)
t.show(t.root) # 1 2 3 5 7 8 9
print()
t.delete(9)
t.show(t.root) # 1 2 3 5 7 8
print()
t.insert(4)
t.insert(13)
t.insert(12)
t.show(t.root) # 1 2 3 4 5 7 8 12 13
print()
t.delete(2)
t.show(t.root) # 1 3 4 5 7 8 12 13
print()
t.insert(6)
t.show(t.root) # 1 3 4 5 6 7 8 12 13