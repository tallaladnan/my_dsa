from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()
    
    def append(self, data):
        self.deque.append(data)
    
    def prepend(self, data):
        self.deque.appendleft(data)
    
    def pop(self):
        if not self.is_empty():
            return self.deque.pop()
        raise IndexError("Deque is empty!")
    
    def shift(self):
        if not self.is_empty():
            return self.deque.popleft()
        raise IndexError("Deque is empty!")
    
    def peek(self):
        if not self.is_empty():
            return self.deque[0]
        raise IndexError("Deque is empty!")
    
    def peek_end(self):
        if not self.is_empty():
            return self.deque[-1]
        raise IndexError("Deque is empty!")
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)
    
    def print_deque(self):
        print(list(self.deque))


dq = Deque()
dq.append(10)
dq.prepend(5)
dq.append(15)

print("Deque contents:")
dq.print_deque()  # Output: [5, 10, 15]

print("\nPeek front:", dq.peek())        # Output: 5
print("Peek end:", dq.peek_end())        # Output: 15

dq.pop()
print("\nAfter pop:")
dq.print_deque()  # Output: [5, 10]

dq.shift()
print("\nAfter shift:")
dq.print_deque()  # Output: [10]

print("\nSize of deque:", dq.size())     # Output: 1
print("Is deque empty?", dq.is_empty())  # Output: False

# Uncomment to see error handling
# dq.shift()
# dq.shift()
# dq.pop()  # Raises IndexError: Deque is empty!
