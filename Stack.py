class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
        
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
        
    def clear(self):
        self.stack.clear()

    def __str__(self):
        return "Stack: " + str(self.stack)

# Create a stack
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Print the stack
print(s)  # Output: Stack: [10, 20, 30]

# Peek the top element
print("Peek:", s.peek())  # Output: Peek: 30

# Pop elements
print("Popped:", s.pop())  # Output: Popped: 30
print("Popped:", s.pop())  # Output: Popped: 20

# Check the size
print("Size:", s.size())  # Output: Size: 1

# Clear the stack
s.clear()
print("After clearing:", s)  # Output: Stack: []

# Check if empty
print("Is empty?", s.is_empty())  # Output: Is empty? True
