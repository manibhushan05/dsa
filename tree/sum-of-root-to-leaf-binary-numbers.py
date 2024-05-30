# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                self.result += int("".join(list(map(str, path))), 2)
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        self.result = 0
        dfs(root, [])
        return self.result
