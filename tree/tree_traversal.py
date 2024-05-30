from collections import deque
from typing import Optional

from tree.tree_helper import build_tree, TreeNode


def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=" ")
        inorder_recursive(root.right)


def preorder_recursive(root):
    if root:
        print(root.val, end=" ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)


def postorder_recursive(root):
    if root is not None:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=" ")


def level_order_traversal(root: Optional[TreeNode]):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


if __name__ == '__main__':
    root = build_tree('[3,9,20,null,null,15,7]')
    # print("Inorder recursive Traversal: ")
    # inorder_recursive(root)
    # print("\nPreorder recursive traversal: ")
    # preorder_recursive(root)
    # print("\nPostorder recursive traversal: ", )
    # postorder_recursive(root)
    print("\nLevel order traversal: ", level_order_traversal(root))
