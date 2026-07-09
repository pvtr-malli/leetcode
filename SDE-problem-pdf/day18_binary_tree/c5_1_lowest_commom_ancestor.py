"""
--problem--
-----------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
 p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

--example--
-----------
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

--link--
--------
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


complexity
-----------
MEDIUM

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from curses import noecho


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            # if we got the any on of the node in question -- we can return that node.
            return root
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)
        # if any one (left,right) None --return another.
        if left == None:
            
            return right
        if right == None:
            return left
        # if both is node none -- we git the lowest ancestor -- so return that.
        else:
            return root





# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""