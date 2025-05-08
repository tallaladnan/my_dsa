from collections import deque

class RingQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full!"
        elif self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
    
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty!"
        data = self.queue[self.front]
        if self.rear == self.front:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data
    
    def peek(self):
        if self.front == -1:
            return "Queue is empty!"
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def current_size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.size - self.front + self.rear + 1
 
    def clear(self):
        self.front = self.rear = -1
        self.queue = [None] * self.size
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty!"
        result = []
        i = self.front
        while True:
            result.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return " -> ".join(result)

# Create a circular queue of size 5
cq = RingQueue(5)

# Enqueue some elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

# Print the queue
print("Queue after enqueue operations:")
print(cq)  # Output: 10 -> 20 -> 30

# Dequeue an element
print("\nDequeued:", cq.dequeue())  # Output: 10

# Peek at the front
print("Front element:", cq.peek())  # Output: 20

# Enqueue more elements
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # Should print "Queue is full!"

# Print the queue
print("\nQueue after more enqueue operations:")
print(cq)  # Output: 20 -> 30 -> 40 -> 50

# Clear the queue
cq.clear()
print("\nQueue after clearing:")
print(cq)  # Output: Queue is empty!
