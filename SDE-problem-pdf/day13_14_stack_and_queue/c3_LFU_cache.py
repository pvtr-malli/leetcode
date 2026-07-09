
"""
--problem--
-----------
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

--example--
-----------
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

--link--
--------
https://leetcode.com/problems/lfu-cache/


complexity
-----------
HARD

"""

class Node:
    def __init__(self, key, val) -> None:
        self.val = val 
        self.key = key
        self.freq = 1 # always keep the first frep as 1.
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self) -> None:
        self.list_size = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.list_size -= 1

    def add_node(self, newnode):
        # add node right after head.
        head_next = self.head.next

        self.head.next = newnode
        newnode.next = head_next
        newnode.prev = self.head
        head_next.prev = newnode
        self.list_size += 1

    def print_linked_list(self):
        node = self.head
        while not node.next == None:
            print("[",node.key, node.val,"]", end='-->')
            node = node.next

        print()

class LFUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.freq_map = {}
        self.key_map = {}
        self.size = 0 
        self.min_freq = 0
    
    def put(self, key, val):
        if self.capacity == 0: return 0

        if key in self.key_map:
            #get the node from key map.
            node = self.key_map[key]
            # get the freqency linkedlist.
            node.val = val
            self.update_node(node)

        else:
            
            # if the LRU is full.
            if self.size == self.capacity:
                # need to delete the LFU element. if 1>more LFU elements remove LRU in it.
                linked_list = self.freq_map[self.min_freq]
                # remove the node from key map.
                del self.key_map[linked_list.tail.prev.key]
                # remove the node from linked list.
                linked_list.remove_node(linked_list.tail.prev)
                
                self.size -= 1
            self.size += 1
            # reset the min_freq
            self.min_freq = 1
            new_node = Node(key, val)
            # get the linkedlist .
            new_list = self.freq_map.get(self.min_freq, DLinkedList())
            new_list.add_node(new_node)

            # update the hash maps
            self.key_map[key] = new_node
            self.freq_map[1] = new_list



    def get(self, key):
        # if the key present in key map.
        if key in self.key_map:
            node = self.key_map[key]
            # update the node
            self.update_node(node)
            return node.val
        # if the key not present return -1.
        return -1

    def update_node(self, node):
        # get the linkedlist from the freq_map.
        current_freq = node.freq
        linked_list = self.freq_map[current_freq]
        # remove the node from old linked list
        linked_list.remove_node(node)

        # update the min_freq.
        if current_freq == self.min_freq and linked_list.list_size == 0:
            self.min_freq += 1
        # increase the frequency.
        node.freq += 1
        # add the node to the new frequency linkedlist.
        new_list = self.freq_map.get(node.freq, DLinkedList())
        new_list.add_node(node)
        self.freq_map[node.freq] = new_list

l = LFUCache(capacity=2)
l.put(1,2)
l.put(2,2)
ll = l.freq_map[1]
ll.print_linked_list()
l.put(3,3)
ll = l.freq_map[1]
ll.print_linked_list()
print(l.get(2))
ll = l.freq_map[1]
ll.print_linked_list()
ll = l.freq_map[2]
ll.print_linked_list()
l.put(4,4)
ll = l.freq_map[1]
ll.print_linked_list()
ll = l.freq_map[2]
ll.print_linked_list()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)