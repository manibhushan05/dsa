# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.result += node.left.val
            dfs(node.left)
            dfs(node.right)

        self.result = 0
        dfs(root)
        return self.result
