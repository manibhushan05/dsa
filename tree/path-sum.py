# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from tree.tree_helper import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True if root.val == targetSum else False
        if self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
                root.right, targetSum - root.val
        ):
            return True
        return False
