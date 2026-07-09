"""
--problem--
-----------
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


--example--
-----------
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

--link--
--------
https://leetcode.com/problems/balanced-binary-tree/


complexity
-----------
EASY

"""

class Solution:
    def isBalanced(self, root):
        return self.maxDepth(root) != -1
    def maxDepth(self, root):
        if root == None:
            return 0
        left_height = self.maxDepth(root.left)
        if left_height == -1: return -1
        right_height = self.maxDepth(root.right)
        if right_height == -1: return -1
        if abs(right_height - left_height) > 1: return -1

        return 1 + max(left_height, right_height)







# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""