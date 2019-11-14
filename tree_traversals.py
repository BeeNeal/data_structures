#         1
#     2     3
#   4   5   



class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  


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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)
print('\n')
preorder(root)
print('\n')
postorder(root)
