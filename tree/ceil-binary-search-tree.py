class Solution:
    def getSuccessor(self, root, val):
        ceil = None
        while root:
            if root.val == val:
                root = root.right
            elif root.val < val:
                root = root.right
            else:
                ceil = root
                root = root.left

        return ceil

