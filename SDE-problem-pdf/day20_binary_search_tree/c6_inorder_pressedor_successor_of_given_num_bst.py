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

def find_predecessor(root, k):
    predecessor = None
    while root != None:
        if root.val == k:
            root = root.left
        elif root.val > k:
            root = root.left
        else:
            predecessor = root.val
            root = root.right
    return predecessor

def find_successor(root, k):
    successor = None
    while root != None:
        # if you find the answer , lets check on its right -- if we have any greater value.
        if root.val == k:
            root = root.right
        # key is smaller -- so move left.
        elif root.val > k:
            successor = root.val
            root = root.left
        # key is biger than root -- i need something big -- so move right
        else:
            root = root.right
    return successor

# same as 
# def find_successor(root, k):
#     successor = None
#     while root != None:
#         # key is smaller -- so move left.
#         if root.val <= k:
#             root = root.right
#         # key is biger than root -- i need something big -- so move right
#         else:
#             successor = root.val
#             root = root.left
#     return successor


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
      
    ans = find_predecessor(root, 22)
    print("Floor of 23", ans)

    ans = find_successor(root, 22)
    print("Ceil of 23", ans)






# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""