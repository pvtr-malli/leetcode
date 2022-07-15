"""
--problem--
-----------
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

--example--
-----------
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []

--link--
--------
https://leetcode.com/problems/binary-tree-right-side-view/


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
class Solution:
    def rightSideView(self, root):
        ans = []
        self.right_view_rec(root, 0, ans)
        return ans
        
    def right_view_rec(self, root,level,ans):
        # gonna use the reversed pre order traversal.
        # Root Right Left
        if root == None:
            return
        # when we traver the first node in a level from right -- the ans size will match with level.
        if level == len(ans):
            ans.append(root.val)
        self.right_view_rec(root.right, level+1, ans)
        self.right_view_rec(root.left, level+1, ans)


class Solution:
    def leftSideView(self, root):
        ans = []
        self.left_view_rec(root, 0, ans)
        return ans
        
    def left_view_rec(self, root,level,ans):
        # gonna use the reversed pre order traversal.
        # Root Right Left
        if root == None:
            return
        # when we traver the first node in a level from right -- the ans size will match with level.
        if level == len(ans):
            ans.append(root.val)
        self.left_view_rec(root.left, level+1, ans)
        self.left_view_rec(root.right, level+1, ans)
        



# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(height of a tree)

# output
"""

"""