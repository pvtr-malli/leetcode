"""
--problem--
-----------
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

--example--
-----------


--link--
--------
# no linke see note


complexity
-----------


"""
def root_to_node_path(root, node_value):
    ans =[]
    root_node_path_help(root, node_value, ans)
    return ans

def root_node_path_help(root, node_val, ans):
    if root == None:
        return False
    ans.append(node_val)
    # if the node is qual to the one we are looking for
    if root.val == node_val:
        return True
    # if any of the left and right call return true -- means we found the path -- return true
    if root_node_path_help(root.left, node_val, ans) or root_node_path_help(root.right, node_val, ans):
        return True
    # if we can't find the node in the current path -- 
    # backtracking -- need to remove the added last path node.
    ans.pop()
    return False







# time and space complexity
# -------------------------
# time -->  O(n)
# space ->  O(n)

# output
"""

"""