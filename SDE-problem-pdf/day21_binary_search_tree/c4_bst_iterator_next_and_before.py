"""
--problem--
-----------
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

--example--
-----------
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

--link--
--------
https://leetcode.com/problems/binary-search-tree-iterator/


complexity
-----------
MEDIUM

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        if root == None: return None
        self.fill_all_left(root)
        print(self.stack)

    def next(self) -> int:
        ele = self.stack.pop()
        if ele.right:
            self.fill_all_left(ele.right)
        return ele.val

    def hasNext(self) -> bool:
        # true if stack not empty , false if empty
        return (False if len(self.stack) == 0 else True)

    def fill_all_left(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left

class BSTIteratorBefore:

    def __init__(self, root):
        self.stack = []
        if root == None: return None
        self.fill_all_right(root)
        print(self.stack)

    def before(self) -> int:
        ele = self.stack.pop()
        if ele.left:
            self.fill_all_right(ele.left)
        return ele.val

    def hasbefore(self) -> bool:
        # true if stack not empty , false if empty
        return (False if len(self.stack) == 0 else True)

    def fill_all_right(self, root):
        while root != None:
            self.stack.append(root)
            root = root.right


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Tree node class
class TreeNode:
      
    def __init__(self, key):
          
        self.val = key
        self.left = None
        self.right = None

# Driver Code
if __name__=='__main__':
      
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

      
    bst=BSTIterator(root)
    print(bst.next())
    print(bst.next())
    print(bst.hasNext())
    print(bst.next())
    print(bst.hasNext())
    print(bst.next())
    print(bst.hasNext())
    print(bst.next())
    print(bst.hasNext())


    bst=BSTIteratorBefore(root)
    print(bst.before())
    print(bst.before())
    print(bst.hasbefore())
    print(bst.before())
    print(bst.hasbefore())
    print(bst.before())
    print(bst.hasbefore())
    print(bst.before())
    print(bst.hasbefore())



# time and space complexity
# -------------------------
# time --> O(1)
# space -> O(height node of tree)

# output
"""

"""