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

    def is_empty(self):
        return len(self.items) == 0
    
def reverse_string(s: str) -> str:
    stack = Stack()  # Create a new stack
    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)
    
    reversed_str = ''
    # Pop each character from the stack and build the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Test the function
input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: "olleh"


