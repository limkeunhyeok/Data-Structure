class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current = self.head

        for c in string:
            if c not in current.children:
                current.children[c] = Node(c)
            current = current.children[c]
        current.data = string
    
    def search(self, string):
        current = self.head

        for c in string:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        if (current.data != None):
            return True
    
    def starts_with(self, prefix):
        current = self.head
        result = []
        subtrie = None

        for c in prefix:
            if c in current.children:
                current = current.children[c]
                subtrie = current
            else:
                return None

        queue = list(subtrie.children.values())
        
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)            
            queue += list(curr.children.values())
        return result
