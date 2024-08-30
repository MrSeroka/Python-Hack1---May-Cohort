class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    
    def is_empty(self):
        return len(self.items) == 0

class QueueWithStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
    
    def enqueue(self, x: int):
        self.stack_in.push(x)
    
    def dequeue(self) -> int:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        
        # Now pop from stack_out
        if not self.stack_out.is_empty():
            return self.stack_out.pop()
        else:
            raise IndexError("dequeue from an empty queue")

# Example usage
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.enqueue(3)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
