"""
--problem--
-----------
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

--example--
-----------
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

--link--
--------
https://leetcode.com/problems/minimum-depth-of-binary-tree/


complexity
-----------
EASY

"""

# since we want minimum path and returning zero if null node -- if won't do that level of if elif
# it will return the min as zero always and return 1 + 0 ==> 1

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        if left_height == 0 and right_height == 0:
            ans = 0
        elif left_height == 0 :
            ans = right_height
        elif right_height == 0:
            ans = left_height
        else:
            ans = min(left_height, right_height)
        return 1 + ans





# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""