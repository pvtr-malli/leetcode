"""
--problem--
-----------
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


--example--
-----------
 Return the root of the tree...............

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

--link--
--------
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


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
    def buildTree(self, preorder, inorder):
        inoreder_map = {}
        # creating a inorder map  -- show that we can get the index of the elements quickly.
        for ind, ele in enumerate(inorder):
            inoreder_map[ele] = ind
        root = self.construct_tree(preorder, 0, len(preorder)-1 ,
                                    inorder, 0 , len(inorder)-1, inoreder_map)
        return root
    def construct_tree(self, preorder, preorder_start_ind, preorder_end_ind,
                             inorder, inorder_start_ind, inorder_end_ind, inorder_map):
        if preorder_start_ind > preorder_end_ind or inorder_start_ind > inorder_end_ind:
            return None
        
        # create the root of the tree.
        root = TreeNode(preorder[preorder_start_ind])

        inorder_root_ind = inorder_map.get(root.val)
        num_left = inorder_root_ind - inorder_start_ind

        root.left = self.construct_tree(preorder, preorder_start_ind + 1, preorder_start_ind + num_left,
                                        inorder, inorder_start_ind, inorder_root_ind - 1, inorder_map)
        root.right = self.construct_tree(preorder, preorder_start_ind +num_left + 1,preorder_end_ind,
                                        inorder,  inorder_root_ind + 1,inorder_end_ind, inorder_map)

        return root
        

 





# time and space complexity
# -------------------------
# time --> O(n)[inorder map] + O(n)[traversal] + O(1)[map accessing]
# space -> O(n)[inorder map] + O(n)[axilaory inside space]

# output
"""

"""