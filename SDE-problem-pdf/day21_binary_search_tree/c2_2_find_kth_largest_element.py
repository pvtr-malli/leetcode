"""
--problem--
-----------


--example--
-----------


--link--
--------
# no link


complexity
-----------


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_num_of_nodes(self, root):
        # use inorder to count the number of nodes in a tree.
        if root == None:
            return 0
        l_num_nodes = self.find_num_of_nodes(root.left)
        r_num_nodes = self.find_num_of_nodes(root.right)
        return 1 + l_num_nodes + r_num_nodes

    def kthLargest(self, root, k):
        # morris traversal not working correctly for this problem
        # gonna use the ierative inorder solution.
        num_nodes = self.find_num_of_nodes(root)
        s = [] # lifo
        count = 0
        # update  k ==> kth largest = (num_nodes - k)th smallest
        k = num_nodes - k + 1
        while True:
            if root != None:
                s.append(root)
                root = root.left
            else:
                if len(s) == 0:
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
        ans=Solution().kthLargest(root,i)
        print(ans) # [5, 8, 10, 3, 14, 20, 4, 22, 25] this is inorder







# time and space complexity
# -------------------------
# time --> O(n) + O(n)[finding nodes]
# space -> O(n)

# output
"""
25
22
4
20
14
3
10
8
5
"""