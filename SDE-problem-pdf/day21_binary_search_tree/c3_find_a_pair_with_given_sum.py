"""
--problem--
-----------
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.

--example--
-----------
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

--link--
--------
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


complexity
-----------
EASY

"""

# since inorder of binary search tree is in sorted order -- gonna use the next and before function here

# merging next and before methods 
# for next reversed is false -- before reversed is true
from curses import noecho


class BSTIterator:

    def __init__(self, root, reverse = False):
        self.stack = []
        self.reverse = reverse
        if root == None: return None
        self.fill_all_values(root)

    def next(self) -> int:
        ele = self.stack.pop()
        if self.reverse:
            self.fill_all_values(ele.left)
        else:
            self.fill_all_values(ele.right)
        return ele.val

    def hasNext(self) -> bool:
        # true if stack not empty , false if empty
        return (False if len(self.stack) == 0 else True)

    def fill_all_values(self, root):
        while root != None:
            self.stack.append(root)
            if self.reverse: 
                root = root.right
            else:
                root = root.left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:
        if root == None: return False
        next_pointer = BSTIterator(root)
        before_pointer = BSTIterator(root, reverse=True)
        i = next_pointer.next()
        j = before_pointer.next()
        while i < j:
            if i + j < k:
                i = next_pointer.next()
            elif i+j > k:
                j = before_pointer.next()
            else:
                return True
        return False





# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(Height of tree) * 2

# output
"""

"""