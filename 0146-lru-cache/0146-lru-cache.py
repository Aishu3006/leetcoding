class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.prev = prv
        node.next = nxt
        prv.next = nxt.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key,val)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]