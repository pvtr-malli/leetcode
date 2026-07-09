"""
--problem--
-----------
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 --example--
-----------
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

--link--
--------
https://leetcode.com/problems/same-tree/


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


class Solution:
    def isSameTree(self, p, q) -> bool:
        # we can use any traversal -- i am using pre order. 
        if p == None or q == None:
            return p == q
        # if two node values same move to left and right.
        if p.val == q.val:
            l_node_same = self.isSameTree(p.left, q.left)
            r_node_same = self.isSameTree(p.right, q.right)
            return l_node_same and r_node_same
        else:
            # if not -- return False.
            return False


# simplified version

class Solution:
    def isSameTree(self, p, q) -> bool:
        # we can use any traversal -- i am using pre order. 
        if p == None or q == None:
            return p == q
        # if two node values same move to left and right.
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""