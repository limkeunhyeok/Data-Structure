# 덱(deque)

![덱](https://user-images.githubusercontent.com/38815618/87896375-044e7a80-ca83-11ea-8558-1f336ec0fa78.PNG)

- 양쪽에서 모두 입출력이 가능한 자료구조
- 스택과 큐에 비해 자유도가 높은 자료구조
- 덱은 double ended queue의 약자로 양방향 큐라는 의미를 가지고 있다.
- 보통 스케줄링에 사용하며, 스케줄링이 복잡해질수록 큐나 스택보다 덱이 더 효율이 잘나오는 경우가 있다.

## 구현

### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.frontLink = None
        self.rearLink = None
```

- frontLink는 해당 노드 앞에 있는 노드와 연결한다.
- rearLink는 해당 노드 뒤에 있는 노드와 연결한다.
  - 1, 2, 3이 있다면, 2에서 frontLink는 1과 연결되고 rearLink는 3과 연결된다.

### Deque Class

- push_front(data): 덱의 맨 앞에 노드 삽입
- pop_front(): 덱의 맨 앞의 노드를 삭제 및 반환
- push_rear(data): 덱의 맨 뒤에 노드 삽입
- pop_rear(): 덱의 맨 뒤의 노드를 삭제 및 반환
- show(): 덱에 저장된 모든 노드를 맨 앞 기준으로 출력

```python
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
```
