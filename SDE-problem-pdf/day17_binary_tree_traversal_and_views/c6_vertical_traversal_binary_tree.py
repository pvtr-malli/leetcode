"""
--problem--
-----------
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

--example--
-----------
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
--link--
--------
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


complexity
-----------
HARD

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from operator import le
import queue

# see link for exampl -- see note for how i indexed

class Solution:
    def verticalTraversal(self, root):
        queue = []
        ans = []
        vertical_and_level_index = {}
        queue.append((root, 0, 0)) # keeping the order as ( node , row, col)
        while not len(queue) == 0:
            tup = queue.pop()
            node = tup[0]
            x,y = tup[1], tup[2]

            # place the node in the correct vertical and level place.
            # dict = {vertical_index: {level_index: [node.val,node.val], }, vertical_index: {level_index: [node.val,node.val], }}
            # d = {0: {0:[1]}, {1:[2]}, 1:{1:[23]} }
            if x in vertical_and_level_index:
                if y in vertical_and_level_index[x]:
                    vertical_and_level_index[x][y].append(node.val)
                else: 
                    vertical_and_level_index[x].update({y:[node.val]})
            else:
                vertical_and_level_index[x] = {y: [node.val]}

            # push the node to the queue.
            if node.left != None: queue.append((node.left, x-1, y+1)) # if left vertical -1 , level + 1
            if node.right != None: queue.append((node.right, x+1, y+1)) # if right -- vertical + 1, level + 1
        print(vertical_and_level_index)
        # loop over the index dict and fill the ans.
        sorted_vertical = sorted(vertical_and_level_index.keys())
        # traverse the sorted vertical indexses.
        for vertical in sorted_vertical:
            # need to sort the level indexes.
            sorted_level = sorted(vertical_and_level_index[vertical].keys())
            a = []
            for level  in sorted_level:
                # we have multiple node in a same (vertical, level) place -- if so, we should sort it and add.
                if len(vertical_and_level_index[vertical][level]) > 1:
                    node_list = sorted(vertical_and_level_index[vertical][level])
                    for val in node_list:
                        a.append(val)
                else:
                    a.append(vertical_and_level_index[vertical][level][0])
            ans.append(a)
        return ans


# RUN BELOW CODE TO UNDERSTAND THE LOOPING
# ==========================================
# vertical_and_level_index = {0: {0: [3], 2: [15,10]}, 1: {1: [20]}, 2: {2: [7]}, -1: {1: [9]}}
# ans = []
# sorted_vertical = sorted(vertical_and_level_index.keys())
# print(sorted_vertical)
# for vertical in sorted_vertical:
#     sorted_level = sorted(vertical_and_level_index[vertical].keys())
#     a = []
#     for level  in sorted_level:
#         node_list = sorted(vertical_and_level_index[vertical][level])
#         for val in node_list:
#             a.append(val)
#     ans.append(a)
# print(ans)



# time and space complexity
# -------------------------
# time --> O(n)[tree traversal] + O(n)[dict traversal]
# space -> O(n) [dict space] + o(n) [queue space]

# output
"""
for Example 1:
[[9],[3,15],[20],[7]]
"""