class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        prv = self.right.prev
        nxt = self.right

        node.prev = prv
        node.next = nxt
        prv.next = nxt.prev = node
    
    def get(self, key):
        if key in self.map.keys():
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return self.map[key].val
        
        return -1
    
    def put(self, key, val):
        if key in self.map.keys():
            self.remove(self.map[key])
        node = Node(key, val)
        self.map[key] = node
        self.insert(node)

        if len(self.map)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]
