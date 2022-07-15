"""
--problem--
-----------
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

--example--
-----------
Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

--link--
--------
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#


complexity
-----------
MEDIUM

"""
#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
#from sortedcontainers import SortedDict # we can use this in real life not in gfg
from click import version_option


class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        q = []
        ans =[]
        level_dict = {}
        q.append((root, 0))
        while not len(q)==0:
            ele = q.pop(0)
            node, vertical = ele[0], ele[1]
            
            # push the node to vertical map , if the vetical index is not already present.
            if vertical not in level_dict:
                level_dict[vertical] = node.data
            if node.left != None:
                q.append((node.left, vertical-1))
            if node.right != None:
                q.append((node.right, vertical+1))
        sorted_key = sorted(level_dict.keys())
        for key in sorted_key:
            ans.append(level_dict[key])
        return ans






# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""