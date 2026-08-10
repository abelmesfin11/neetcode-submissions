class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key : Node
        self.cap = capacity
        self.size = 0

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add_left(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_left(node)
            node.val = value
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.add_left(newNode)
            self.size += 1

            if self.size > self.cap:
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]
                self.size -= 1

        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def add_left(self, node):
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node
        node.prev = self.left














        
