from tree.tree_helper import build_tree


def is_children_sum_property(root):
    if root is None or (root.left is None and root.right is None):
        return True
    left_val = 0
    right_val = 0
    if root.left:
        left_val = root.left.val
    if root.right:
        right_val = root.right.val
    return left_val + right_val == root.val and is_children_sum_property(root.left) and is_children_sum_property(
        root.right)


if __name__ == '__main__':
    root = build_tree('[5,2,3]')
    print(is_children_sum_property(root))
