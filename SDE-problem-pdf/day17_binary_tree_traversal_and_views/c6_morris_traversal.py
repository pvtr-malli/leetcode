def morris_traversal_inorder(root):
        # gonna use the marrio traversal to reduce the space complexcity.
        inorder = []
        cur = root
        while cur != None:
            if cur.left == None:
                inorder.append(cur.val)
                cur = cur.right
            else:
                
                prev = cur.left
                while prev.right != None and prev.right != cur:
                    prev =prev.right
                # we are moving left for the first time. -- in this case it won't have the thread
                if prev.right == None:
                    # create the thread
                    prev.right = cur
                    cur = cur.left
                # if prev.right eqaul to cur means we are in the thread -- need to remove it and move right.
                else:
                    # add the root 
                    inorder.append(cur.val)
                    prev.right = None
                    cur = cur.right
        return inorder

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

    ans=morris_traversal_inorder(root)
    print(ans) # [5, 8, 10, 3, 14, 20, 4, 22, 25]