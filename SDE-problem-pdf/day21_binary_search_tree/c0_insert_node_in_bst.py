"""
--problem--
-----------
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

--example--
-----------
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]


Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
--link--
--------
https://leetcode.com/problems/insert-into-a-binary-search-tree/


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
    def insertIntoBST(self, root, val):
        # do a binary search kinf of a thing, find the correct place having NUll -- insert it there.
        if root == None:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val < val:
                if cur.right != None:
                    cur = cur.right
                else:
                    # insert the node here.
                    cur.right = TreeNode(val)
                    return root 
            else:
                if cur.left != None:
                    cur = cur.left
                else:
                    # insert the node here.
                    cur.left = TreeNode(val)
                    return root
        # when you find a correct null place -- insert a node there.

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
      
    ans=Solution().insertIntoBST(root, 12)
    inorder = morris_traversal_inorder(ans)
    print(inorder)


# time and space complexity
# -------------------------
# time --> O(log n)
# space -> O(1)

# output
"""

"""