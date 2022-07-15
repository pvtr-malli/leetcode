"""
--problem--
-----------
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder
 is the postorder traversal of the same tree, construct and return the binary tree.

--example--
-----------
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


--Constraints--
---------------
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.


--link--
--------
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


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
    def buildTree(self, inorder, postorder):
        inoreder_map = {}
        # creating a inorder map  -- show that we can get the index of the elements quickly.
        for ind, ele in enumerate(inorder):
            inoreder_map[ele] = ind
        root = self.construct_tree(postorder, 0, len(postorder)-1 ,
                                    inorder, 0 , len(inorder)-1, inoreder_map)
        return root
    
    def construct_tree(self, postorder, post_start, post_end,
                        inorder, in_start, in_end, inorder_map):
        if post_start > post_end or in_start > in_end:
            return None

        # create the root of the tree.
        root = TreeNode(postorder[post_end])

        inorder_root_ind = inorder_map.get(root.val)
        num_left = inorder_root_ind - in_start

        root.left = self.construct_tree(postorder, post_start, post_start + num_left -1,
                                        inorder, in_start, inorder_root_ind - 1, inorder_map)
        root.right = self.construct_tree(postorder, post_start +num_left,post_end - 1,
                                        inorder,  inorder_root_ind + 1,in_end, inorder_map)

        return root




# time and space complexity
# -------------------------
# time --> O(n) + O(n)
# space -> O(n) + O(n)

# output
"""

"""