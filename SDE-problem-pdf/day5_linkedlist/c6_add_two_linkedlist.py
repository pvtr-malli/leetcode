"""
--problem--
-----------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

--example--
-----------
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

--link--
--------
https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        step 1 - l1.val + l2.val + carry ( all not None)
        step 2 - new_node_value = sum % 10 (get the remainder)
        step 3 - carry = sum / 10 (get the 2ed didigt)
        step 4 - create a new node and add it to linked list with val = new_node_value
        step 5 - stop this when all l1,2,carry becomes None
        """
        carry = 0
        head_prev = ListNode(val = 0, next = None)
        tmp = head_prev
        while (l1 != None) or (l2 != None) or (carry!=0):
            # step 1 - l1.val + l2.val + carry ( all not None)
            print("l1",l1,"\n")
            print("l2",l2,"\n")
            sum = 0
            if l1 != None:
                sum += l1.val
            if l2 != None:
                sum += l2.val
            if carry != 0:
                sum += carry
            print("sum",sum,"\n")
            # step 2 - new_node_value = sum % 10 (get the remainder)
            new_node_val = sum % 10
            # step 3 - carry = sum / 10 (get the 2ed didigt)
            carry = sum // 10
            print("new node val",new_node_val,"\n")
            print("carry",carry,"\n")
            # step 4 - create a new node and add it to linked list with val = new_node_value
            new_node = ListNode(val= new_node_val, next= None)
            tmp.next = new_node
            print("head_prev", head_prev, "\n")
            if l1!= None: l1 = l1.next
            if l2!= None: l2 = l2.next
            tmp = tmp.next
        return head_prev.next






# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""
l1 ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}} 

l2 ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}} 

sum 7 

new node val 7 

carry 0 

head_prev ListNode{val: 0, next: ListNode{val: 7, next: None}} 

l1 ListNode{val: 4, next: ListNode{val: 3, next: None}} 

l2 ListNode{val: 6, next: ListNode{val: 4, next: None}} 

sum 10 

new node val 0 

carry 1 

head_prev ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: None}}} 

l1 ListNode{val: 3, next: None} 

l2 ListNode{val: 4, next: None} 

sum 8 

new node val 8 

carry 0 

head_prev ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}} 


"""