"""
--problem--
-----------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

--example--
-----------
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

--link--
--------
https://leetcode.com/problems/validate-binary-search-tree/


complexity
-----------
MEDIUM

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def isValidBST(self, root):
        return self.validate_rec(root, -sys.maxsize - 1 , sys.maxsize)
    
    def validate_rec(self, node, min_range, max_range):
        if node == None:
            return True
        if node.val <= min_range  or node.val >= max_range :
            return False

        l_call = self.validate_rec(node.left, min_range, node.val)
        r_cal = self.validate_rec(node.right, node.val, max_range)
        return l_call and r_cal 





# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[axilory]

# output
"""

"""