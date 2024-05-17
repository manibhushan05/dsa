class QueueUsingArray:
    def __init__(self, capacity):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return element

    def front_element(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        current = self.front
        while current != self.rear:
            print(self.queue[current], end=" ")
            current = (current + 1) % self.capacity
        print(self.queue[self.rear])


# Example usage:
queue = QueueUsingArray(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.print_queue()  # Output: 10 20 30 40 50
queue.dequeue()
queue.dequeue()
queue.print_queue()  # Output: 30 40 50
queue.enqueue(60)
queue.enqueue(70)
queue.print_queue()  # Output: 30 40 50 60 70
