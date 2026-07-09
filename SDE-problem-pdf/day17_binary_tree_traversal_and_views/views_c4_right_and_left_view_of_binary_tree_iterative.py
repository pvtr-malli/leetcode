"""
--problem--
-----------


--example--
-----------


--link--
--------

# no linke for this 

complexity
-----------


"""

class Solution:
    def rightSideView(self, root):
        ans = []
        q = []
        if root == None: return ans
        q.append((root, 0))
        while not len(q) == 0:
            ele = q.pop(0)
            node , level = ele[0], ele[1]
            # if the level == len(ans) we are visiting the first node of the level from right.
            if level == len(ans):
                ans.append(node.val)
            # we are gonna traverse right first and left next.
            if node.right != None:
                q.append((node.right, level + 1))
            if node.left != None:
                q.append((node.left, level + 1))
            print(ans)
            print(q)
        return ans

class Solution:
    def leftSideView(self, root):
        ans = []
        q = []
        if root == None: return ans
        q.append((root, 0))
        while not len(q) == 0:
            ele = q.pop(0)
            node , level = ele[0], ele[1]
            # if the level == len(ans) we are visiting the first node of the level from right.
            if level == len(ans):
                ans.append(node.val)
            # we are gonna traverse left first and right next.
            if node.left != None:
                q.append((node.left, level + 1))
            if node.right != None:
                q.append((node.right, level + 1))
            
            print(ans)
            print(q)
        return ans

# Tree node class
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
      
    print("Bottom view of the given binary tree :")
      
    ans=Solution().rightSideView(root)
    print(ans)



# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n) almost

# output
"""
Bottom view of the given binary tree :
[20]
[(<__main__.Node object at 0x7f2909515b50>, 1), (<__main__.Node object at 0x7f2909515a30>, 1)]
[20, 22]
[(<__main__.Node object at 0x7f2909515a30>, 1), (<__main__.Node object at 0x7f2909515d60>, 2), (<__main__.Node object at 0x7f2909515d00>, 2)]
[20, 22]
[(<__main__.Node object at 0x7f2909515d60>, 2), (<__main__.Node object at 0x7f2909515d00>, 2), (<__main__.Node object at 0x7f2909515ca0>, 2), (<__main__.Node object at 0x7f2909515c40>, 2)]
[20, 22, 25]
[(<__main__.Node object at 0x7f2909515d00>, 2), (<__main__.Node object at 0x7f2909515ca0>, 2), (<__main__.Node object at 0x7f2909515c40>, 2)]
[20, 22, 25]
[(<__main__.Node object at 0x7f2909515ca0>, 2), (<__main__.Node object at 0x7f2909515c40>, 2)]
[20, 22, 25]
[(<__main__.Node object at 0x7f2909515c40>, 2), (<__main__.Node object at 0x7f2909515eb0>, 3), (<__main__.Node object at 0x7f2909515e50>, 3)]
[20, 22, 25]
[(<__main__.Node object at 0x7f2909515eb0>, 3), (<__main__.Node object at 0x7f2909515e50>, 3)]
[20, 22, 25, 14]
[(<__main__.Node object at 0x7f2909515e50>, 3)]
[20, 22, 25, 14]
[]
[20, 22, 25, 14]
"""