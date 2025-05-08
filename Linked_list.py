class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
            
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def shift(self):
        if self.size == 0:
            print("Linked List is already empty!")
        else:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            
    def pop(self):
        if self.size == 0:
            print("Linked List is already empty!")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.size -= 1
            
    def remove_position(self, position):
        if position < 0 or position >= self.size:
            print("Out of bound")
            return
        if position == 0:
            self.shift()
        elif position == self.size - 1:
            self.pop()
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self.size -= 1
        
    def insert_position(self, data, position):
        if position < 0 or position > self.size:
            print("Out of bound")
            return
        if position == 0:
            self.prepend(data)
        elif position == self.size:
            self.append(data)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            self.size += 1
        
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
        
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
        
    def get_length(self):
        return self.size
        
    def is_empty(self):
        return self.size == 0
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head
        
    def get_node_at(self, position):
        if position < 0 or position >= self.size:
            print("Out of bound")
            return None
        current = self.head
        for _ in range(position):
            current = current.next
        return current
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


ll = LinkedList()
ll.append(5)
ll.append(10)
ll.prepend(1)
ll.insert_position(7, 2)

print("List after insertions:")
ll.print_list()  # Output: 1 -> 5 -> 7 -> 10

print("\nSearch for 7:", ll.search(7))  # Output: 2
print("Search for 15:", ll.search(15))  # Output: -1

ll.reverse()
print("\nList after reversing:")
ll.print_list()  # Output: 10 -> 7 -> 5 -> 1

ll.remove_position(1)
print("\nList after removing position 1:")
ll.print_list()  # Output: 10 -> 5 -> 1

print("\nIs list empty?", ll.is_empty())  # Output: False
print("List size:", ll.get_length())  # Output: 3

ll.clear()
print("\nList after clearing:")
ll.print_list()  # Output: (empty)
