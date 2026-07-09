"""
--problem--
-----------
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

--example--
-----------
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
--link--
--------
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


complexity
-----------
HARD

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = []
        string = ""
        if root == None:
            return ""
        q.append(root)
        string = string + str(root.val) +","
        while not len(q) == 0:
            ele = q.pop(0)
            # add the left element -- put X if that is None.
            if ele.left != None:
                q.append(ele.left)
                string = string + str(ele.left.val) + ","
            else:
                string = string + "X" +","
            # add the right element -- put X if that is None.
            if ele.right != None:
                q.append(ele.right)
                string = string + str(ele.right.val) + ","
            else:
                string = string + "X" + ","
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        arr = data.split(",")[:-1] # the last element would be empty sting becaseu of the last comma -- ['20', '8', '22', '5', '3', 'X', 'X', 'X', 'X', 'X', 'X', ''] -- so we are leaving it
        q = []
        # crate a root node and append to queue.
        root = TreeNode(arr[0])
        q.append(root)    
        starting_position = 1 
        while not len(q) ==0:
            ele = q.pop(0)
            # add the left node if that is not none.
            if arr[starting_position] != "X":
                # create a new node.
                left_node = TreeNode(arr[starting_position])
                # add to queue.
                q.append(left_node)
                # add to tree.
                ele.left = left_node
            # add the right node if that is not none.
            if arr[starting_position + 1] != "X":
                # create a new node.
                right_node = TreeNode(arr[starting_position + 1])
                # add to queue.
                q.append(right_node)
                # add to tree.
                ele.right = right_node
            # update the starting_position
            starting_position += 2

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

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
    root.left.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(25)
    # root.left.right.left = TreeNode(10)
    # root.left.right.right = TreeNode(14)

    s=Codec().serialize(root)
    print(s)
    ans = Codec().deserialize(s)
    print(ans)



# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""