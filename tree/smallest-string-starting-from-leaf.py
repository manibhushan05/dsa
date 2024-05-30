# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        alphabet = list('abcdefghijklmnopqrstuvwxyz')

        def dfs(node, path):
            if node is None:
                return
            path.append(alphabet[node.val])
            if node.left is None and node.right is None:
                result.append("".join(list(map(str, reversed(path)))))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        result = []
        dfs(root, [])
        result.sort()
        return result[0]
