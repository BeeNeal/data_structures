class TreeNode:
    """ """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def find_range_sum(root, l, r):
        """ """

        if not root:
            return 0
        elif root.val < l:
            return self.find_range_sum(root.r, l, r)
        elif root.val > r:
            return self.find_range_sum(root.l, l, r)
        return root.val + self.find_range_sum(root.r, l, r) + self.find_range_sum(root.l, l, r)

    # iterative approach
    # def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    #     stk, sum = [root], 0
    #     while stk:
    #         node = stk.pop()
    #         if node:
    #             if node.val > L:
    #                 stk.append(node.left)    
    #             if node.val < R:
    #                 stk.append(node.right)
    #             if L <= node.val <= R:
    #                 sum += node.val    
    #     return sum