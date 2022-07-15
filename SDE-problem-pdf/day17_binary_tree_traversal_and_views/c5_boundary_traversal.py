# No leedcode question available.

def isLeaf(node):
    return node.left == None and node.right == None

def left_boundary(root, ans):
    while isLeaf(root) == False:
        if root.left != None:
            ans.append(root.left)
            root = root.left
        elif root.right != None:
            ans.append(root.right)
            root = root.right

def leaf_nodes(node,ans):
    if isLeaf(node):
        ans.append(node.val)
        return
    if node.left != None: leaf_nodes(node.left, ans)
    if node.right != None: leaf_nodes(node.right, ans)

def right_boundary(root, ans):
    cur = root.right
    temp = []
    while cur != None:
        if isLeaf(cur) == False: temp.append(cur.val)
        if cur.right != None: cur = cur.right
        else: cur = cur.left

    # append back the result from temp to ans
    for i in range(len(temp)):
        ans.append(temp.pop())

def boundary_traversal(root):
    ans = []
    if root == None: return 
    if isLeaf(root) == False: ans.append(root.val)
    left_boundary(root, ans)
    leaf_nodes(root, ans)
    right_boundary(root, ans)
    return ans