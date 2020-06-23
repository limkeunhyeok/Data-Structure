from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, rank, data):
        heappush(self.queue, (rank, data))
    
    def dequeue(self):
        if not self.queue:
            return 'empty'
        return heappop(self.queue)
    
    def show(self):
        print(self.queue)

pq = PriorityQueue()
print(pq.dequeue())
pq.show()
pq.enqueue(1, 'd')
pq.enqueue(1, 'c')
pq.enqueue(2, 'b')
pq.enqueue(4, 'a')
pq.enqueue(3, 'e')
pq.show()
print(pq.dequeue()) # (1, c)
print(pq.dequeue()) # (1, d)
pq.show()