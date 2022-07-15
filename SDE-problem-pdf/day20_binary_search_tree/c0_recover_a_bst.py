"""
--problem--
-----------
You are given the root of a binary search tree (BST),
where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

--example--
-----------
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

--Constraints--
---------------

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1

--link--
--------
https://leetcode.com/problems/recover-binary-search-tree/


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
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [TreeNode(-sys.maxsize-1)]
        first = [None]
        mid = [None]
        second = [None]
        first_node , second_node = self.recoverTreeHelper(root, prev, first, mid, second)
        print(first_node, second_node)
        # swap two node values.
        first_node[0].val , second_node[0].val = second_node[0].val, first_node[0].val

    def recoverTreeHelper(self, root, prev, first, mid, second):
        # gonna do inorder.
        if root == None: return None
        # go left
        self.recoverTreeHelper(root.left, prev, first, mid, second)
        # we are at root. copare the root value with prev and if it violies the rule save it.
        # for a valid BST -- previous node value should be lesser than next node value.
        if root.val < prev[0].val and prev[0] != None:
            if first[0] == None:
                first[0] = prev[0]
                mid[0] = root
            else:
                second[0] = root
        prev[0] = root
        self.recoverTreeHelper(root.right, prev, first, mid, second)
        # at the end return first and second swappable element.
        return first, second if second[0] != None else mid
        




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""