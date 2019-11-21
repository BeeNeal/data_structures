#         1
#     2     3
#   4   5   


# Binary Tree Node
class BTNode: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  

# Binary Tree Traversals
def inorder(root):
    """Traverse the tree in left, root, right order. """

    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

def preorder(root):
    """Traverse the tree in root, left, right order. 
    
    Used to create a copy of the tree
    """

    if root:
        print(root.val),
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """Traverse tree in left, right, root order.        
    
    Used to delete the tree
    """

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

root = BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)
root.left.left = BTNode(4)
root.left.right = BTNode(5)
# inorder(root)
# print('\n')
# preorder(root)
# print('\n')
# postorder(root)

def find_max_node_in_bst(root):
    """Return val of rightmost node, which in a BST will be the greatest num."""

    while root.right:
        root = root.right
    return root.val

bt_root = BTNode(16)
bt_root.left = BTNode(10)
bt_root.right = BTNode(17)
bt_root.right.right = BTNode(21)
bt_root.left.left = BTNode(4)
bt_root.left.right = BTNode(5)
bt_root.left.left.left = BTNode(1)
print(inorder(bt_root))
print('Max val is: \n')
print(find_max_node_in_bst(bt_root))

class Node:

    def __init__(self, val):
        self.val = val
        self.children = []

# trees/graphs are made from an ordering of nodes


# find if subtree in tree
def is_match(tree, subtree):
    """ """

    if not(tree and subtree):
        return tree is subtree
    return (subtree.val == tree.val and
            is_match(tree.left, subtree.left) and
            is_match(tree.right, subtree.right))

def is_subtree(tree, subtree):
    """ """

    if is_match(tree, subtree):
        return True
    if not subtree:
        return False
    return is_subtree(subtree.left, tree) or is_sutree(subtree.right, tree)


# iterate through tree, have a dictionary 

subtrees = {}
current = self.root
while current:
    if