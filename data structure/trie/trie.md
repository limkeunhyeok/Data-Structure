# 트라이(trie)

- 트라이는 문자열 집합을 표현하는 자료구조
- 원하는 원소 작업을 O(n)에 해결할 수 있는 자료구조

![트라이](https://user-images.githubusercontent.com/38815618/86514197-9df31680-be4b-11ea-829c-38092f41a496.PNG)

- 루트 노드가 되는 최상위 노드에는 어떠한 단어도 들어가지 않고, 루트 아래 노드부터 문자열의 접두사가 하나씩 나타난다.
- 저장 공간이 크다는 단점이 있다.
  - 최종 메모리는 O(포인터 크기 x 포인터 배열 개수 x 트라이에 존재하는 총 노드의 개수)

## 구현

참고: <https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0>

### Node class

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
```

- key는 단어의 글자 하나를 담는 데 이용한다.
- data는 마지막 글자를 나타내주는 flag이다.
  - jack의 경우 j > a > c > k에서 마지막 글자인 k 노드의 data에만 jack이 들어가고, 그 외 노드의 data에는 None값으로 둔다.

### Trie class

- insert(string): 트라이에 문자열 삽입
- search(string): 주어진 단어 string이 트라이에 존재하는지 여부 반환
- starts_with(prefix): 주어진 prefix 로 시작하는 단어들을 BFS로 트라이에서 찾아 리스트 형태로 반환

```python
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
```
