class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(leet_code_input: str, should_print_tree_code_to_console=False):
    if leet_code_input == '[]':
        return
    leet_code_input = leet_code_input.replace(' ', '')
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]
    for index, current_node in enumerate(leet_code_input[1:]):
        if current_node != 'null':
            if index & 1:
                nodes.append((nodes[index // 2][0] + '.right', current_node))
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))
    root = TreeNode(int(nodes[0][1]))
    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        if should_print_tree_code_to_console:
            print(execution_statement)
        exec(execution_statement)
    return root
