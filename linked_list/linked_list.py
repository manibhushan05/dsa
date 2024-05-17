class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end="->")
            current_node = current_node.next
        print('None')

    def is_empty(self):
        return self.head is None

    def append(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        if self.is_empty():
            return

        if self.head.val == val:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.val != val:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def len_of_list(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def check_if_exists(self, val):
        current_node = self.head
        while current_node:
            if current_node.val == val:
                return True
            current_node = current_node.next
        return False

    def convert_array_to_linked_list(self, nums):
        if len(nums) == 0:
            return
        self.head = ListNode(nums[0])
        mover = self.head
        for num in nums[1:]:
            mover.next = ListNode(num)
            mover = mover.next

    def reverse_linked_list(self):
        current_node = self.head
        prev_node = None
        while current_node and current_node.next:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.convert_array_to_linked_list([10, 20, 30, 40])
    linked_list.reverse_linked_list()
    linked_list.print_list()
