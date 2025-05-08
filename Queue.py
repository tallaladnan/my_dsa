class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty!"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty!"
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        
    def __str__(self):
        if self.is_empty():
            return "Queue is empty!"
        return " -> ".join(map(str, self.queue))

# Create a queue
q = Queue()

# Enqueue elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Print the queue
print("Queue after enqueue operations:")
print(q)  # Output: 1 -> 2 -> 3

# Dequeue an element
print("\nDequeued:", q.dequeue())  # Output: 1

# Peek at the front element
print("Front element:", q.peek())  # Output: 2

# Check if the queue is empty
print("Is queue empty?", q.is_empty())  # Output: False

# Print the current size
print("Current size:", q.size())  # Output: 2

# Clear the queue
q.clear()
print("\nQueue after clearing:")
print(q)  # Output: Queue is empty!
