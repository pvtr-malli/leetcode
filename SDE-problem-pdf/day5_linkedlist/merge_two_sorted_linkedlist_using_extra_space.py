"""
--problem--
-----------
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

--example--
-----------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

--link--
--------
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # define the first rules.
        if list1 == None: return list2
        elif list2 == None: return list1
        # set 2 pointes
        result_node = ListNode(val = 0,next=None) # ListNode is --defined by leedcode stuff
        result_list = ListNode(val = 0,next=None)
        p1, p2 = list1, list2
        while p1.next != None or p2.next != None:
            # if value from pl small.
            if p1.val < p2.val:
                new_node = ListNode(val = p1.val,next=None)
                # add the new node to the last node.
                result_list.next = 
                p1 = p1.next
            else:
                result_node.next = p2
                p2 = p2.next
        # something balance in list1 add those
        if p1.next != None:
            while pl.next != None:

        