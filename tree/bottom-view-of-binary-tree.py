from collections import deque


class Solution:
    def bottomView(self, root):
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
        bottom_view = {}
        for row, col, val in node_list:
            bottom_view[col] = val
        return [bottom_view[hd] for hd in sorted(bottom_view)]

