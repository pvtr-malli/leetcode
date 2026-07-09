"""
--problem--
-----------
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

--example--
-----------
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

--link--
--------
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


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
    def zigzagLevelOrder(self, root):
        queue = []
        ans = []
        if root == None: return
        queue.append(root)
        flag = 0
        while not len(queue) == 0:
            queue_size = len(queue)
            level_arr = [-1] * queue_size
            # if flag 0 --> we are traversing from left - right. so indez should be 0 - n
            index = range(queue_size)
            if flag == 1:
                # if flag 1 --> we are traversing from right - left. so indez should be n-1 - 0
                index = range(queue_size-1, -1, -1)
            for i in index:
                ele = queue.pop(0)
                # put the ele in level array.
                level_arr[i] = ele.val
                if ele.left != None: queue.append(ele.left)
                if ele.right != None: queue.append(ele.right)
            # cahnge the flag.
            flag = (0 if flag == 1 else 1)
            ans.append(level_arr)
        return ans





# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""