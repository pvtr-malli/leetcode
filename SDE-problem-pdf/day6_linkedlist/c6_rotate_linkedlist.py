"""
--problem--
-----------
Given the head of a linked list, rotate the list to the right by k places.

--example--
-----------
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

in k=1  -- [5,1,2,3,4]
in k=2  -- [4,5,1,2,3]

--link--
--------
https://leetcode.com/problems/rotate-list/


complexity
-----------
MEDIUM

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        """
        oppservation 1: number of rotation needed = k % len (because k = len rotation given the original list --> so k multiplcation (eg: if k=5 then 5 10 15 20 ) will give the original list)
        step 1: Find the length of the linkelist.
        step 2: Now i at the end of the linked list -- Connect it to the head to make a circular list.
        step 3: Break the connection at len-k th position.

        """
        if head == None:
            return head
        i = head
        length = 1 # should start from 1
        # step 1: Find the length of the linkelist.
        while i.next != None:
            i = i.next
            length += 1
        # step 2: Now i at the end of the linked list -- Connect it to the head to make a circular list.
        i.next = head
        print("Length of the list", length)
        print("i starting position",i)
        # step 3: Break the connection at len-k th position.
        k = k % length
        brack_position = length - k
        print("breaking point ",brack_position)
        while brack_position:
            i = i.next
            brack_position -= 1
        
        # break the connection.
        head = i.next
        i.next = None
        print("Now after braking head",head)
        return head






# time and space complexity
# -------------------------
# time --> O(N)
# space -> O(1)

# output
"""
Length of the list 5
i starting position Error - Found cycle in the ListNode
breaking point  3
Now after braking head ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}}}

"""