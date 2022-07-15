"""
--problem--
-----------
Given the root of a binary search tree, and an integer k,
 return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

--example--
-----------
Input: root = [3,1,4,null,2], k = 1
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

--link--
--------
https://leetcode.com/problems/kth-smallest-element-in-a-bst/


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
    def kthSmallest(self, root, k):
        # morris traversal not working correctly for this problem
        # gonna use the ierative inorder solution.
        s = [] # lifo
        count = 0
        while True:
            if root != None:
                s.append(root)
                root = root.left
            else:
                if  len(s) == 0:
                    break
                root = s.pop()
                # we got the root val so count it.
                count+=1
                if count == k:
                    return root.val
                root = root.right

class Node:
      
    def __init__(self, key):
          
        self.val = key
        self.left = None
        self.right = None

# Driver Code
if __name__=='__main__':
      
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    for i in range(1,10):
        ans=Solution().kthSmallest(root,i)
        print(ans) # [5, 8, 10, 3, 14, 20, 4, 22, 25]


# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[stack]

# output
"""

"""