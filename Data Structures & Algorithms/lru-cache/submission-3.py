'''
capacity = 2
What if you have the case where {1 = 10, 2 = 20} lrucache.put(1, 30)
{1 = 30, 2 = 20} lrucache.put(3, 0)
nnono the capacity means the entire cache (hashmap) 
first idea: we use a hashmap as a cache, linked list as a tracker to see which key-value
pair was last touched (head of linked list). This doesn't work because it would be O(C)
where C is the capacity since we have to iterate through all the elements within the linked
list to remove and add something to the end.

looking at hints: use a double linked list where we have a hashmap of key -> node and
'''

class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    

class LRUCache:

    # cache key -> node
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start

    def add_end(self, node):
        prev, nxt = self.end.prev, self.end
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # start <-> 1 <-> 2 <-> end
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val
            self.remove(self.cache[key])
            self.add_end(self.cache[key])
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add_end(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.start.next
            self.remove(self.start.next)
            del self.cache[lru.key]
            




