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
from tkinter import N


def change_tree(root):
    if root == None:
        return
    child_sum = 0
    if root.left != None:
        child_sum += root.left.val
    if root.right != None:
        child_sum += root.right.val
    if root.val >= child_sum:
        root.val = child_sum
    else:
        if root.left != None:
            root.left.val = child_sum
        if root.right != None:
            root.right.val= child_sum
    change_tree(root.left)
    change_tree(root.right)

    # backtracking 
    tot = 0
    if root.left != None:
        tot += root.left.val
    if root.right != None:
        tot += root.right.val
    if root.left != None or root.right != None: 
        root.val = tot
    







# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""