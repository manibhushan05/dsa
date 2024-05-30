from collections import deque

import pytest

from tree.tree_helper import build_tree


def binary_tree_zigzag_level_order_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    flipper = False
    while queue:
        level_nodes = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flipper:
            result.append(level_nodes[::-1])
        else:
            result.append(level_nodes)
        flipper = not flipper
    return result


def test_binary_tree_zigzag_level_order_traversal():
    root = build_tree('[3,9,20,null,null,15,7]')
    assert binary_tree_zigzag_level_order_traversal(root) == [[3], [20, 9], [15, 7]]

    root = build_tree('[1]')
    assert binary_tree_zigzag_level_order_traversal(root) == [[1]]

    root = build_tree('[]')
    assert binary_tree_zigzag_level_order_traversal(root) == []


if __name__ == '__main__':
    pytest.main()
