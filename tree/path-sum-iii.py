# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, targetSum, path):
            if node is None:
                return
            path.append(node.val)
            targetSum -= node.val
            if targetSum == 0:
                self.result += 1
            dfs(node.left, targetSum, path)
            dfs(node.right, targetSum, path)
            path.pop()

        def traverse(node, targetSum):
            if node:
                dfs(node, targetSum, [])
                traverse(node.left, targetSum)
                traverse(node.right, targetSum)

        self.result = 0
        traverse(root, targetSum)
        return self.result
