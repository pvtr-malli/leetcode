"""
--problem--
-----------


--example--
-----------


--link--
--------



complexity
-----------


"""


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
            level_dict[vertical] = node.data
            print(level_dict)
            if node.left != None:
                q.append((node.left, vertical-1))
            if node.right != None:
                q.append((node.right, vertical+1))
            print(q)
        sorted_key = sorted(level_dict.keys())
        for key in sorted_key:
            ans.append(level_dict[key])
        return ans

# Tree node class
class Node:
      
    def __init__(self, key):
          
        self.data = key
        self.hd = float('inf')
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
      
    print("Bottom view of the given binary tree :")
      
    ans=Solution().topView(root)
    print(ans)




# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""