"""
--problem--
-----------
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

--example--
-----------
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

--link--
--------
https://leetcode.com/problems/middle-of-the-linked-list/

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        # use the slow and fast tortoise method.
        # slow moves by one
        # fast moves by 2 steps
        # when fast reches the end -- slow will be in the middle.
        slow,fast = head, head
        print("head",head)
        while (fast !=None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next

            print("slow",slow)
            print("fast",fast)
        return slow 


#3 printed Solution
"""
head ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

slow ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
fast ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}

slow ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
fast ListNode{val: 5, next: None}


"""
        