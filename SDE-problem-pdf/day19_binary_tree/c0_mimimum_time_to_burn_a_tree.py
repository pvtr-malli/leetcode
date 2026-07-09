"""
--problem--
-----------
Problem Description

Given a binary tree denoted by root node A and a leaf node B from this tree.

 It is known that all nodes connected to a given node (left child, right child and parent) get burned in 1 second. Then all the nodes which are connected through one intermediate get burned in 2 seconds, and so on.

You need to find the minimum time required to burn the complete binary tree.



Problem Constraints
2 <= number of nodes <= 105

1 <= node value, B <= 105

node value will be distinct



Input Format
First argument is a root node of the binary tree, A.

Second argument is an integer B denoting the node value of leaf node.



Output Format
Return an integer denoting the minimum time required to burn the complete binary tree.

--example--
-----------
Example Input
Input 1:

 Tree :      1 
            / \ 
           2   3 
          /   / \
         4   5   6
 B = 4
Input 2:

 Tree :      1
            / \
           2   3
          /     \
         4       5 
 B = 5 

Example Explanation
Explanation 1:

 After 1 sec: Node 4 and 2 will be burnt. 
 After 2 sec: Node 4, 2, 1 will be burnt.
 After 3 sec: Node 4, 2, 1, 3 will be burnt.
 After 4 sec: Node 4, 2, 1, 3, 5, 6(whole tree) will be burnt.
 
Explanation 2:

 After 1 sec: Node 5 and 3 will be burnt. 
 After 2 sec: Node 5, 3, 1 will be burnt.
 After 3 sec: Node 5, 3, 1, 2 will be burnt.
 After 4 sec: Node 5, 3, 1, 2, 4(whole tree) will be burnt.
--link--
--------
https://www.interviewbit.com/problems/burn-a-tree/


complexity
-----------
MEDIUM

"""
# +++++++++++++++++++++++++++++++++++++++++++++
# GOT MAXIMIUM RECURSSION LIMIT RESEACHED ERROR :
# +++++++++++++++++++++++++++++++++++++++++++++


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
class Solution:
    def find_node(self, root, target_val):
        if root == None:
            return
        if target_val == root.val:
            return root
        
        ls = self.find_node(root.left, target_val)
        
        if ls == None:
            rs = self.find_node(root.right, target_val)
            return rs
        else:
            return ls
    def find_height(self, root):
        if root == None:
            return 0
        lh = self.find_height(root.left)
        rh = self.find_height(root.right)
        return 1 + max(lh, rh)

    def mark_parent(self, root, parent_map):
        # gona do level order traversal -- bfs 
        q = []
        q.append(root)
        while not len(q) == 0:
            parent = q.pop(0)
            if parent.left != None:
                q.append(parent.left)
                parent_map[parent.left] = parent
            if parent.right != None:
                q.append(parent.right)
                parent_map[parent.right] = parent
    def max_depth(self, root, parent_map, visited):
        # we have a parent map so we can traves to parent also.
        if root == None:
            return 0
        visited[root] = True
        # initialize those 3 element to mimimum value.
        ph = lh = rh = (- sys.maxsize - 1)
        if not visited.get(parent_map.get(root)):
            ph = self.max_depth(parent_map.get(root), parent_map, visited)
        if not visited.get(root.left):
            lh = self.max_depth(root.left, parent_map, visited)
        if not visited.get(root.right):
            rh = self.max_depth(root.right, parent_map, visited)
        return 1 + max(ph, max(lh, rh))
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, root, B):
        # Find the target node.
        if root.val == B:
            node = root
            return self.find_height(root) - 1
        #  marking the parent node.
        parent_map = {}
        self.mark_parent(root, parent_map)
        node = self.find_node(root, B)
        # just keeping this node as a starting point find the max height/depth of the tree.
        visited={}
        return self.max_depth(node, parent_map, visited) - 1 # final ans  max depth - 1


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
    # root.right.left = Node(4)
    # root.right.right = Node(25)
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(14)
       
    ans=Solution().solve(root, 8)
    print(ans)

        




# time and space complexity
# -------------------------
# time --> O(n)[parent maping] + O(n)[finding height]
# space -> O(n)[parent_map] + O(n)[visited map] + O(n)[queue find parent]

# output
"""

"""