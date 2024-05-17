class StackUsingArray:
    def __init__(self, capacity):
        self.top_index = -1
        self.capacity = capacity
        self.stack = []

    def push(self, element):
        if self.is_full():
            print("Stack is full")
            return None
        self.top_index += 1
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        self.top_index -= 1
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index + 1 == self.capacity

    def print_stack(self):
        print(self.stack)


stack = StackUsingArray(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)
stack.print_stack()
