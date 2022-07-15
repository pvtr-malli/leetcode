"""
--problem--
-----------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

--example--
-----------
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

--link--
--------
https://leetcode.com/problems/symmetric-tree/


complexity
-----------
EASY

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from fcntl import F_SEAL_SEAL
from logging import root

class Solution:
    def isSymmetric(self, root):
        return root != None and self.symmetric_check(root.left, root.right)
    def symmetric_check(self, left, right):
        if left == None or right ==None:
            return left == right
        if left.val != right.val: return False
        left_call = self.symmetric_check(left.left, right.right)
        right_call= self.symmetric_check(left.right, right.left)
        return left_call and right_call






# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n) worst case when the tree is skewed

# output
"""

"""