"""
--problem--
-----------
Given the head of a singly linked list, reverse the list, and return the reversed list.



--example--
-----------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

but you have to return the head of the list -- that is enough 

--link--
--------
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input format of linked list
# head ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
class Solution():
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # basically reversing the links
        tmp_node = None
        print("list", head)
        while head != None:
            next_node = head.next
            head.next = tmp_node
            
            # move tmp and head
            tmp_node = head
            head = next_node
            print("head",head)
            print("tmo",tmp_node)
        

        return tmp_node
        

"""
list ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
head ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
tmo ListNode{val: 1, next: None}

head ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
tmo ListNode{val: 2, next: ListNode{val: 1, next: None}}

head ListNode{val: 4, next: ListNode{val: 5, next: None}}
tmo ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}

head ListNode{val: 5, next: None}
tmo ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}

head None
tmo ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}

"""