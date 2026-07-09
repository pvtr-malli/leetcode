"""
--problem--
-----------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

--example--
-----------
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Input: head = [1], n = 1
Output: []


Input: head = [1,2], n = 1
Output: [1]

--link--
--------
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # optimal approach using fast and slow tortoise.
        """
        step 1 - create a new node with zero value and point it's next to head -- used to return the head.
        step 2 - assign slow and fast tortoise to new node.
        step 3 - move fast tortoise n times
        step 4 - and move fats and slow tortoise until fats.next not qual to None.
        step 5 - delete the slow.next node. 
        """
        print("head",head,"n",n)
        # step 1 - create a new node with zero value and point it's next to head -- used to return the head.
        new_node = ListNode(val=0, next=None)
        new_node.next = head
        # step 2 - assign slow and fast tortoise to new node.
        slow = new_node; fast = new_node
        print("slow and fast",slow,fast)
        # step 3 - move fast tortoise n times
        for _ in range(n):
            fast = fast.next

        # edge case
        # if the fast reached last node after moving n times --> means n and lenght of the node is same
        # we need to remove the first element.
        # so simply return the head.next
        if fast.next == None:
            return head.next

        print('fast after moving', fast)
        # step 4 - and move fats and slow tortoise until fats.next not qual to None.
        while fast.next!= None:
            fast = fast.next
            slow = slow.next
        print("slow and fats after moving", slow,fast)
        #  step 5 - delete the slow.next node. 
        slow.next = slow.next.next
        print("head after deletetion",head)
        return new_node.next
       








# time and space complexity
# -------------------------
# time --> O(n) -- only moving the fast to the end is hapening
# space -> O(1)

# output
"""
head ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}} n 2


slow and fast ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}} ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}

fast after moving ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}

slow and fats after moving ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}} ListNode{val: 5, next: None}

head after deletetion ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}}
"""