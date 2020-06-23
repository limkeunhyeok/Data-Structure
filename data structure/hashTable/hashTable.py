class HashTable:
    def __init__(self):
        self.table = [None for i in range(139)]

    def hash_function(self, key):
        return ord(key)
    
    def put(self, key, data):
        self.table[self.hash_function(key)] = data
    
    def find(self, key):
        return self.table[self.hash_function(key)]

ht = HashTable()
ht.put('a', 1234)
ht.put('z', 5344)
ht.put('e', 43)
ht.put('c', 89502)
print(ht.find('z')) # 5344
print(ht.find('e')) # 43
print(ht.find('f')) # None