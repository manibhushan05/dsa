class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def print_dll(head):
    current_node = head
    while current_node:
        print(current_node.data, end=' ')
        current_node = current_node.next
    return head


def constructDLL(arr: [int]) -> Node:
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        current_node = Node(arr[i])
        mover.next = current_node
        current_node.prev = mover
        mover = current_node
    return head


def reverseDLL(head):
    current_node = head
    if current_node is None or current_node.next is None:
        return head
    while current_node:
        prev = current_node.prev
        current_node.prev = current_node.next
        current_node.next = prev
        current_node = current_node.prev
    return prev.prev



arr = [10,20,30,40]
dll = constructDLL(arr)
reverse_dll = reverseDLL(dll)
print_dll(reverse_dll)