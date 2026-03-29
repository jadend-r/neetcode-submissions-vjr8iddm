class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.capacity = capacity
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    # Remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    # Insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            self.remove(self.keyToNode[key])
            self.insert(self.keyToNode[key])
            return self.keyToNode[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.remove(self.keyToNode[key])
        self.keyToNode[key] = Node(key, value)
        self.insert(self.keyToNode[key])

        if len(self.keyToNode) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.keyToNode[lru.key]
