"""
--problem--
-----------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

--example--
-----------
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false


--Constraints--
---------------
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


--link--
--------
https://leetcode.com/problems/symmetric-tree/


complexity
-----------
EASY

"""

class Solution:
    def isSymmetric(self, root):
        return root != None and self.symmetric_check(root.left, root.right)
    def symmetric_check(self, left, right):
        if left == None or right ==None:
            return left == right
        if left.val != right.val: return False
        left_call = self.symmetric_check(left.left, right.right)
        right_call= self.symmetric_check(left.right, right.left)
        return left_call and right_call






# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)

# output
"""

"""