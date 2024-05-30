# https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if root is None:
                return []
            queue = deque([root])
            result = []
            while queue:
                level_nodes = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(level_nodes)
            return result

        result = bfs(root)
        return sum(result[-1])
