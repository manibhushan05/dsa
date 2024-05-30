# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)
                queue.extend(node.children)
            result.append(level_nodes)
        return result
