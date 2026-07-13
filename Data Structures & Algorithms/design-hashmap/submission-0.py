class ListNode:

    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(1000)]
        

    def hash(self, index):
        return (index % len(self.hashmap))
    
    
    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return            
            curr = curr.next
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        curr = self.hashmap[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        curr = self.hashmap[self.hash(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)