class Node:
    def __init__(self, key=None, val=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.cache = {}
        self.left.nxt, self.right.prev = self.right, self.left

    # insert a node on the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt, node.prev = node, prev
        nxt.prev, node.nxt = node, nxt

    # remove a node
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        n = Node(key, value)
        self.cache[key] = n
        self.insert(n)

        if len(self.cache) > self.capacity:
            l = self.left.nxt
            self.remove(l)
            del self.cache[l.key]
