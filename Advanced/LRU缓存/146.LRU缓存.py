class LRUCache:

    def __init__(self, capacity: int):
        self.records = {}

        # only store the key
        self.head = None
        self.last = None


    def get(self, key: int) -> int:

        pass

    def put(self, key: int, value: int) -> None:

        if key in self.records:
            target_node =  self.records[key]
            target_node.val = value

            previous_node = target_node.previous
            next_node = target_node.next

            if previous_node is not None:
                previous_node.next = next_node
            if next_node is not None:
                next_node.previous = previous_node

        else:
            target_node = double_direct_link(value)
            
        first_node = self.records[self.head]

        first_node.previous = target_node
        target_node.next = first_node
        self.head = target_node

        if self.tail is not None:
            self.tail = self.tail.previous



class double_direct_link:
    def __init__(self, val):
        self.previous = None
        self.val = val
        self.next = None

    def __repr__(self):
        return f"[{self.previous} - {self.val} - {self.next}]"

    def __str__(self):
        return self.__repr__()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
