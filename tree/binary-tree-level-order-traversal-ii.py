from collections import deque

import pytest

from tree.tree_helper import build_tree


def binary_tree_leve_order_traversal_ii(root):
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
    return result[::-1]


def test_binary_tree_leve_order_traversal_ii():
    root = build_tree('[1,2,3,null,5,null,4]')
    assert binary_tree_leve_order_traversal_ii(root) == [[5, 4], [2, 3], [1]]

    root = build_tree('[3,9,20,null,null,15,7]')
    assert binary_tree_leve_order_traversal_ii(root) == [[15, 7], [9, 20], [3]]
    
    root = build_tree('[]')
    assert binary_tree_leve_order_traversal_ii(root) == []


if __name__ == '__main__':
    pytest.main()
