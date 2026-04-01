class Node:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.nxt, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt, node.prev = node, prev
        nxt.prev, node.nxt = node, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
