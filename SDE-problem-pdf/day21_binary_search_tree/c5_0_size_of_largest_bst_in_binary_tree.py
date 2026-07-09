"""
--problem--
-----------


--example--
-----------


--link--
--------
# primimum question.


complexity
-----------
HARD

"""


import sys

class Solution:
    def largestBST(self, root) -> int:
        if root == None:
            return 0
        return self.largest_bst(root).max_size
    
    def largest_bst(self, root):
        if root == None:
            return NodeDetails(0, -sys.maxsize - 1, sys.maxsize)

        l_side = self.largest_bst(root.left)
        r_side = self.largest_bst(root.right)

        if l_side.max_val >= root.val or r_side.min_val <= root.val:
            # it is not a valida binary search tree. 
            return NodeDetails(max(l_side.max_size, r_side.max_size), sys.maxsize, -sys.maxsize -1)
        # it is a valid binary tree
        return NodeDetails((1 + l_side.max_size + r_side.max_size), 
                            max(root.val, r_side.max_val),
                            min(root.val, l_side.min_val))


class NodeDetails:
        def __init__(self, max_size, max_val, min_val) -> None:
            self.max_size = max_size
            self.max_val = max_val
            self.min_val = min_val





# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[axilory]

# output
"""

"""