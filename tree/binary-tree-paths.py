# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                result.append("->".join(list(map(str, path))))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        result = []
        dfs(root, [])
        return result
