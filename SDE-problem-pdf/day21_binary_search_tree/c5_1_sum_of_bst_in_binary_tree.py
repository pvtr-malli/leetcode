"""
--problem--
-----------
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

--example--
-----------
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.


Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104

--link--
--------
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

complexity
-----------
HARD

"""

# REWRITE IT -- some wrong test cases



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def maxSumBST(self, root) -> int:
        if root == None:
            return 0
        return self.max_sum_bst(root).max_sum
    
    def max_sum_bst(self, root):
        if root == None:
            return NodeDetails(0, -sys.maxsize - 1, sys.maxsize)

        l_side = self.max_sum_bst(root.left)
        r_side = self.max_sum_bst(root.right)

        if l_side.max_val >= root.val or r_side.min_val <= root.val:
            # it is not a valida binary search tree. 
            if l_side.max_val < 0 and r_side.min_val < 0 and root.val < 0: 
                return NodeDetails(0, sys.maxsize, -sys.maxsize -1)
            return NodeDetails(max(l_side.max_sum, r_side.max_sum), sys.maxsize, -sys.maxsize -1)
        # if all the values in a tree is negative -- then conside it as a not valid BST.
        if l_side.max_val < 0 and r_side.min_val < 0 and root.val < 0: 
            return NodeDetails(0, sys.maxsize, -sys.maxsize -1)
        # it is a valid binary tree
        return NodeDetails((root.val + l_side.max_sum + r_side.max_sum), 
                            max(root.val, r_side.max_val),
                            min(root.val, l_side.min_val))


class NodeDetails:
        def __init__(self, max_sum, max_val, min_val) -> None:
            self.max_sum = max_sum
            self.max_val = max_val
            self.min_val = min_val
        


class Node:
      
    def __init__(self, key):
          
        self.val = key
        self.left = None
        self.right = None

# Driver Code
if __name__=='__main__':

    # root = Node(1)
    # root.left = Node(8)
    # root.left.left = Node(6)
    # root.left.left.left = Node(9)
    # root.left.right = Node(1)
    # root.left.right.left = Node(-5)
    # root.left.right.left.right = Node(-3)
    # root.left.right.right = Node(4)
    # root.left.right.right.right = Node(10)
    root = Node(1)
    root.right = Node(10)
    root.right.left = Node(-5)
    root.right.right= Node(20)


    ans = Solution().maxSumBST(root)
    print(ans)

# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""