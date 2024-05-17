class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.next
        print()

    def print_ll_recursive(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return
        print(node.val, end=" ")
        if node.next is None:
            print()
            return
        self.print_ll_recursive(node.next)

    def convert_array_to_ll(self, nums):
        if len(nums) == 0:
            return
        self.head = ListNode(nums[0])
        node = self.head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next

    def convert_array_to_ll_recursive(self, nums, index=0):
        if index == len(nums):
            return None
        node = ListNode(nums[index])
        node.next = self.convert_array_to_ll_recursive(nums, index + 1)
        if index == 0:
            self.head = node
        return node

    def append_at_end(self, val):
        new_node = ListNode(val)
        node = self.head
        if node is None:
            self.head = new_node
            return
        while node.next:
            node = node.next
        node.next = new_node
        return node

    def append_at_beg(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def delete_node_first_found(self, val):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
            return
        if self.head.val == val:
            self.head = self.head.next
            return

        node = self.head
        while node.next and node.next.val != val:
            node = node.next
        if node.next:
            node.next = node.next.next

    def delete_node_all_occurrence(self, val):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
            return
        if self.head.val == val:
            self.head = self.head.next
        node = self.head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

    def is_empty(self):
        return self.head is None

    def append_at_end_recursive(self, val, node=None):
        if node is None:
            node = self.head

        if node is None:
            self.head = ListNode(val)
            return
        if node.next is None:
            node.next = ListNode(val)
            return
        self.append_at_end_recursive(val, node.next)

    def middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    ll = LinkedList()
    # ll.convert_array_to_ll_recursive([10])
    # middle_node = ll.middle()
    # print(middle_node.val)
    arr = [[2, 3], [1, 2]]
    students = [
        {
            "name": "Mani",
            "age": 31
        },
        {
            "name": "Kumar",
            "age": 37
        },
        {
            "name": "Deepak",
            "age": 30
        }
    ]
    arr.sort(key=lambda x: x[1])
    print(students)
    students.sort(key=lambda x: x["age"])
    print(students)
