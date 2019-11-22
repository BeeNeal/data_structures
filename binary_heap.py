# A property of a complete tree is that can represent with a single list
# in a complete tree, the left child of a parent (at position p) is found in
#  position 2p and right child is 2p + 1
# node at position n means parent is position n/2

class BinaryHeap:
    """Implement a balanced Binary Tree"""

    def __init__(self):
        """Initialize binary heap with single list."""

        # inititalize with a zero so no errors with integer division
        self.heapList = [0]
        self.currentSize = 0
    

    def insert(self, item):
        """adds a new item to the heap"""

        # since is list, could append, however that would violate the heap,
        # so need to do an insertion sort type insertion to insert
        pass

    def findMin():
        """returns the item with the min key value, leaving item in the heap"""

        pass

    def delMin():
        """returns the item w/ min key value, and removes it"""

        pass

    def isEmpty():
        """returns true if the heap is empty"""

        pass

    def size():
        """returns the number of items in the heap"""

        return self.currentSize

    def buildHeap(list):
        """builds a new heap from a list of keys"""

        pass