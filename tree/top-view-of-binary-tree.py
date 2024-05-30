# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

from tree.tree_helper import TreeNode, build_tree


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return []

        queue = deque([(root, 0, 0)])
        node_list = []
        while queue:
            for _ in range(len(queue)):
                node, row, col = queue.popleft()
                node_list.append([row, col, node.val])
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        top_view = {}
        node_list.sort(key=lambda x: x[1])
        for row, col, val in node_list:
            if col not in top_view:
                top_view[col] = val
        return [top_view[hd] for hd in sorted(top_view)]


root = build_tree('[1 ,2, 3, null,4, 5, null, 6, 9, 7, 8, 13, null, null, 11, 14, null, null, 10]')
print(Solution().topView(root))
