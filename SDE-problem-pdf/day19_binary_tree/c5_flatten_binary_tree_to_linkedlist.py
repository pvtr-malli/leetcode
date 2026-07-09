"""
--problem--
-----------
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

--example--
-----------
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


--Constraints--
---------------
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


--link--
--------
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


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

# DEBUG IT
# =========

# class Solution:
#     def flatten(self, root) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         prev = [None]
#         self.flatten_bt(root, prev)
#     def flatten_bt(self, root, prev):
#         if root == None:
#             return
#         self.flatten_bt(root.right, prev)
#         self.flatten_bt(root.left, prev)
#         root.right = prev[0]
#         root.left = None
#         prev = root


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur != None:
            if cur.left != None:
                prev = cur.left
                while(prev.right):
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

# Tree node class
class Node:
      
    def __init__(self, key):
          
        self.data = key
        self.hd = float('inf')
        self.left = None
        self.right = None

# Driver Code
if __name__=='__main__':
      
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)


    ans=Solution().flatten(root)
    print(ans)

# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(1)

# output
"""

"""