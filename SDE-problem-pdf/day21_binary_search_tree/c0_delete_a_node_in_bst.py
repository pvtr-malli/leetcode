"""
--problem--
-----------
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

--example--
-----------
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.



Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105

--link--
--------
https://leetcode.com/problems/delete-node-in-a-bst/


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
    def delete_node(self, root):
        # edge case.
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        right_side = root.right
        right_extreme_node = self.find_extreme_right(root.left)

        # add the right part to the left part's extreme right's right.
        right_extreme_node.right = right_side
        return root.left

    def find_extreme_right(self, root):
        while root.right != None:
            root = root.right
        return root

    def deleteNode(self, root, key):
        if root == None: return root
        if root.val == key:
            return self.delete_node(root)
        root_node = root
        while root != None:
            # see the node in left side.
            if root.val > key:
                if root.left != None and root.left.val == key:
                    root.left = self.delete_node(root.left)
                    break
                else:
                    root = root.left
            # check the node in right side.
            else:
                if root.right != None and root.right.val == key:
                    root.right = self.delete_node(root.right)
                    break
                else:
                    root = root.right
        # if we can't find the node /or if we did any modification return the root objet
        return root_node


def morris_traversal_inorder(root):
        # gonna use the marrio traversal to reduce the space complexcity.
        inorder = []
        cur = root
        while cur != None:
            if cur.left == None:
                inorder.append(cur.val)
                cur = cur.right
            else:
                
                prev = cur.left
                while prev.right != None and prev.right != cur:
                    prev =prev.right
                # we are moving left for the first time. -- in this case it won't have the thread
                if prev.right == None:
                    # create the thread
                    prev.right = cur
                    cur = cur.left
                # if prev.right eqaul to cur means we are in the thread -- need to remove it and move right.
                else:
                    # add the root 
                    inorder.append(cur.val)
                    prev.right = None
                    cur = cur.right
        return inorder

# Tree node class
class TreeNode:
      
    def __init__(self, key):
          
        self.val = key
        self.left = None
        self.right = None

# Driver Code
if __name__=='__main__':
      
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(11)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
      
    ans=Solution().deleteNode(root, 8)
    inorder = morris_traversal_inorder(ans)
    print(inorder)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""