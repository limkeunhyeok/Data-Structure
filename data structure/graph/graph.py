class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, v, w):
        if v not in self.graph:
            self.graph[v] = {w}
        else:
            self.graph[v].add(w)
            set(self.graph[v])
        
        if w not in self.graph:
            self.graph[w] = {v}
        else:
            self.graph[w].add(v)
            set(self.graph[w])

    def show(self):
        for i in self.graph:
            print(i, '->', self.graph[i])

    def dfs(self, start):
        stack = [start]
        marked = [start]
        while stack:
            v = stack.pop()
            print(v, end = ' ')
            for w in self.graph[v]:
                if w not in marked:
                    stack.append(w)
                    marked.append(w)
        print()

    def bfs(self, start):
        queue = [start]
        marked = [start]
        while queue:
            v = queue.pop(0)
            print(v, end = ' ')
            for w in self.graph[v]:
                if w not in marked:
                    queue.append(w)
                    marked.append(w)
        print()


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.show()
g.dfs(1) # 1 4 5 3 2
g.dfs(2) # 2 5 4 3 1
g.bfs(1) # 1 2 3 4 5
g.bfs(2) # 2 1 4 5 3