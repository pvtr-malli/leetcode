"""
--problem--
-----------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

--example--
-----------
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]


Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

--link--
--------
https://leetcode.com/problems/3sum/submissions/


complexity
-----------
MEDIUM

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from curses import noecho


class Solution:
    def copyRandomList(self, head):
        """
        step 1: Create a copy node at the next position of each original node.
        step 2: create the random pointer for the copy node.
        """
        if head == None:
            return None
        # step 1: Create a copy node at the next position of each original node.
        temp = head
        while temp!=None:
            print("temp", temp)
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = temp.next.next
        
        # step 2: create the random pointer for the copy node.
        temp = head
        while temp != None:
            if temp.random == None:
                temp.next.random = None
                temp = temp.next.next
                continue
            temp.next.random = temp.random.next
            temp = temp.next.next
        
        # step 3: break the connection with the original node a separate the copy and original node.
        copy_head = head.next
        cur_copy_ndoe = copy_head
        left_of_copy_node  = head ; right_of_copy_node = head.next.next

        while right_of_copy_node != None:
            cur_copy_ndoe.next = right_of_copy_node.next
            left_of_copy_node.next  = right_of_copy_node
            # move pointers
            left_of_copy_node = left_of_copy_node.next 
            right_of_copy_node = right_of_copy_node.next.next
            cur_copy_ndoe = cur_copy_ndoe.next


        return copy_head


# time and space complexity
# -------------------------
# time --> O(N) + O(N) + O(N) 
# space -> O(1) [copy node space is allowed , so no extra space]

# output
"""
can't see the values -- only the objects so no use of print
temp <__main__.Node object at 0x7f182e37a6b0>
temp <__main__.Node object at 0x7f182e37acb0>
temp <__main__.Node object at 0x7f182e37af80>
temp <__main__.Node object at 0x7f182e37b070>
temp <__main__.Node object at 0x7f182e37b220>

"""