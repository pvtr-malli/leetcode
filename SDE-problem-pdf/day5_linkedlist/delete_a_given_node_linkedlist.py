"""
--problem--
-----------
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

--example--
-----------
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

--link--
--------
https://leetcode.com/problems/delete-node-in-a-linked-list/

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # head is not given. so this approach can be used.
        # copy the next node value to this node 
        print("node",node)
        node.val = node.next.val
        # remove the next node.
        print("node afte copying", node)
        node.next = node.next.next
        print("node after deletion", node)
        # not going to return anything.



# time and space complexity
# -------------------------
# time --> O(1)
# space -> O(1)

# output
"""
node ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}


node afte copying ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}


node after deletion ListNode{val: 1, next: ListNode{val: 9, next: None}}

"""