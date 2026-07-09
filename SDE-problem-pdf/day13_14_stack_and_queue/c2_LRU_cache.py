"""
--problem--
-----------
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

--example--
-----------
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

--link--
--------
https://leetcode.com/problems/lru-cache/


complexity
-----------
HARD

"""


class Node:
    def __init__(self, key, val) -> None:
        self.val = val 
        self.key = key
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, newnode):
        # add node right after head.
        head_next = self.head.next

        self.head.next = newnode
        newnode.next = head_next
        newnode.prev = self.head
        head_next.prev = newnode


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.linked_list = DLinkedList()
        self.key_map = {}

    def get(self, key):
        if key in self.key_map:
            node = self.key_map[key]
            node_val= node.val
            self.linked_list.remove_node(node)
            self.linked_list.add_node(node)
            return node_val
        return -1

    def put(self, key, val):
        if self.size == self.capacity:
            del self.key_map[self.linked_list.tail.prev.key] # delete that node from key map.
            self.linked_list.remove_node(self.linked_list.tail.prev)
            self.size -= 1
        if key in self.key_map:
            node = self.key_map[key]
            node.val = val # update the new value.
            self.linked_list.remove_node(node) # remove from where it was.
            self.linked_list.add_node(node) # add right after head -- since it is accessed now.
        else:
        # adding the new node to the linkedlist and key map.
            self.size += 1
            new_node = Node(key, val)
            self.linked_list.add_node(new_node)
            self.key_map[key] = new_node

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1) # cache is {1=1}
# lRUCache.put(2, 2) # cache is {1=1, 2=2}
# lRUCache.get(1)   # return 1
# lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2) )   # returns -1 (not found)
# lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1)  )  # return -1 (not found)
# print(lRUCache.get(3))    # return 3
# print(lRUCache.get(4))    # return 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

l = LRUCache(2)
l.get(2)
l.put(2,6)
l.get(1)
l.put(1,5)
l.put(1,2)
print(l.get(1))
print(l.get(2))