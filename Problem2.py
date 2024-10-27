class Node:

    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, curr: Node):  # TC = SC = O(1)
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def add_to_head(self, curr: Node):   # TC = SC = O(1)
        curr.prev = self.head
        curr.next = self.head.next
        self.head.next = curr
        curr.next.prev = curr

    def get(self, key: int) -> int:     # TC = SC = O(1)
        if key not in self.hashmap: return -1
        curr = self.hashmap[key]
        self.remove_node(curr)
        self.add_to_head(curr)
        return curr.value

    def put(self, key: int, value: int) -> None:  # TC = SC = O(1)
        if key in self.hashmap:
            self.hashmap[key].value = value
            curr = self.hashmap[key]
            self.remove_node(curr)
            self.add_to_head(curr)
        else:
            if len(self.hashmap) == self.capacity:
                tailPrev = self.tail.prev
                self.remove_node(tailPrev)
                del self.hashmap[tailPrev.key]

            curr = Node(key, value)
            self.add_to_head(curr)
            self.hashmap[key] = curr

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)