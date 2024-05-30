# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return (
            1 + max(self.minDepth(root.left), self.minDepth(root.right))
            if root.left is None or root.right is None
            else 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        )
