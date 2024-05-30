# https://leetcode.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compute_height(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, height: int, node: TreeNode) -> bool:
        left, right = 0, 2 ** height - 1
        for _ in range(height):
            pivot = (left + right) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        height = self.compute_height(root)
        if height == 0:
            return 1
        left, right = 1, 2 ** height - 1
        while left <= right:
            pivot = (left + right) // 2
            if self.exists(pivot, height, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return 2 ** height - 1 + left
