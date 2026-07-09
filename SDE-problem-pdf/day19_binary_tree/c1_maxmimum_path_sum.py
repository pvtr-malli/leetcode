"""
--problem--
-----------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

--example--
-----------
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

--link--
--------
https://leetcode.com/problems/binary-tree-maximum-path-sum/


complexity
-----------
HARD

"""
import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        maxi = [-sys.maxsize-1]
        self.max_sum(root, maxi)
        return maxi[0]
    def max_sum(self,root,maxi):
        if root == None:
            return 0
        left_sum = max(0, self.max_sum(root.left, maxi))
        right_sum = max(0, self.max_sum(root.right, maxi))
        maxi[0] = max(maxi[0], root.val + left_sum + right_sum )
        return root.val + max(left_sum, right_sum)






# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""