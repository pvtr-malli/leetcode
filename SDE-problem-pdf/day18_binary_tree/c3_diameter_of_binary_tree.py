"""
--problem--
-----------
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

--example--
-----------
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

--link--
--------
https://leetcode.com/problems/diameter-of-binary-tree/


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
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.maxDepth(root, diameter)
        return diameter[0]
    
    def maxDepth(self, root, diameter):
        if root == None:
            return 0
        left_height = self.maxDepth(root.left, diameter)
        right_height = self.maxDepth(root.right, diameter)
        # diameter is the left height + right height.
        diameter[0] = max(diameter[0], left_height + right_height)

        return 1 + max(left_height, right_height)







# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""