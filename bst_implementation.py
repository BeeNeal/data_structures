class Node:
    """Has recursive functions that does most the heavy lifting"""

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data)

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        """ """
        # prevent duplicates
        if self.value == data:
            return False
        elif self.value > data:
            

        # checks if there is a node in the tree
        if self.root:
            # recursive - 
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True



        pass

    def preorder(self):
    def postorder(self):
    def inorder(self):
