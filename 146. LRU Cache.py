class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:

        if key in self.map:
            node = self.map[key]
            if node != self.tail:
                if node == self.head:
                    self.head = self.head.next
                else:
                    node.pre.next = node.next
                    node.next.pre = node.pre
                self.tail.next = node
                node.pre = self.tail
                node.next = None
                self.tail = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value  # update value
            if node != self.tail:
                if node == self.head:
                    self.head = self.head.next
                else:
                    node.pre.next = node.next
                    node.next.pre = node.pre
                self.tail.next = node
                node.pre = self.tail
                node.next = None
                self.tail = node

        else:
            new_node = Node(key, value)
            if self.capacity == 0:
                temp = self.head
                head = self.head.next
                self.map.pop(temp.key)
                self.capacity += 1
            if not self.head and not self.tail:
                self.head = new_node
            else:
                self.tail.next = new_node
                new_node.next = self.tail
                new_node.next = None
            self.tail = new_node
            self.map[key] = new_node
            self.capacity -= 1

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

####################
class LRUCache:

    def __init__(self, capacity: int):
        self.hash_table = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.hash_table:
            node = self.hash_table[key]
            self.delete(node)
            self.put_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.delete(self.hash_table[key])
        node = Node(key, value)
        self.put_to_head(node)
        if self.capacity < len(self.hash_table):
            temp = self.tail.pre
            self.delete(temp)

    def delete(self, node):
        # hold a temp
        temp = node.next
        # delete node
        pre_node = node.pre
        pre_node.next = temp
        temp.pre = pre_node
        # delete from hash
        del self.hash_table[node.key]

    def put_to_head(self, node):
        # add to hash
        self.hash_table[node.key] = node
        # hold a temp
        temp = self.head.next
        # add node
        self.head.next = node
        node.pre = self.head
        node.next = temp
        temp.pre = node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
print(obj.get(1))
print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
