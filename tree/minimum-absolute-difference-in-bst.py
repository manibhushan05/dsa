# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)

        result = []
        inorder(root)
        mini = float("inf")
        for i in range(1, len(result)):
            mini = min(mini, abs(result[i] - result[i - 1]))
        return mini
