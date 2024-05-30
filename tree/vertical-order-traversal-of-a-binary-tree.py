from collections import OrderedDict, deque
from typing import Optional, List

from tree.tree_helper import TreeNode, build_tree


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []

        def bfs(root):
            queue = deque([(root, 0, 0)])
            while queue:
                for _ in range(len(queue)):
                    node, row, col = queue.popleft()
                    node_list.append([row, col, node.val])
                    if node.left:
                        queue.append((node.left, row + 1, col - 1))
                    if node.right:
                        queue.append((node.right, row + 1, col + 1))

        bfs(root)
        node_list.sort(key=lambda x: (x[1], x[2]))
        result = OrderedDict()
        for row, col, val in node_list:
            result.setdefault(col, []).append(val)
        return list(result.values())


root = build_tree('[3,9,20,null,null,15,7]')
print(Solution().verticalTraversal(root))
