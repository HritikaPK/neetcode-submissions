class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #mapping key to DLL nodes

        # to identify most and least recent additions
        self.left, self.right = Node(0,0), Node(0,0)

        # left - least ; right - most 
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        #remove from left
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self,node):
        # insert at right
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #TODO: update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove old key-val pair
            self.remove(self.cache[key])
        #insert new key-va pair
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from LRU from DLL and delete LRU from Hmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

              
