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


from curses import keyname


def find_floor(root, k):
    floor = -1
    while root != None:
        if root.val == k:
            floor = k
            return floor
        elif root.val > k:
            root = root.left
        else:
            floor = root.val
            root = root.right
            
    return floor


def find_ceil(root, k):
    ceil = -1
    while root != None:
        if root.val == k:
            ceil = k
            return ceil
        elif root.val > k:
            ceil = root.val
            root = root.left
        else:
            root = root.right
    return ceil


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
      
    ans = find_floor(root, 23)
    print("Floor of 23", ans)

    ans = find_ceil(root, 23)
    print("Floor of 23", ans)


# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""