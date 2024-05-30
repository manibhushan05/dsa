from collections import deque

import pytest

from tree_helper import build_tree


def binary_tree_level_order_traversal(root):
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


def test_binary_tree_level_order_traversal():
    root = build_tree('[1,2,3,null,5,null,4]')
    assert binary_tree_level_order_traversal(root) == [[1], [2, 3], [5, 4]]

    root = build_tree('[1,null,3]')
    assert binary_tree_level_order_traversal(root) == [[1], [3]]

    root = build_tree('[]')
    assert binary_tree_level_order_traversal(root) == []


if __name__ == "__main__":
    pytest.main()
