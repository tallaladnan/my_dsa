class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, current, data):
        if current.data > data:
            if current.left:
                self._insert(current.left, data)
            else:
                current.left = Node(data)
        else:
            if current.right:
                self._insert(current.right, data)
            else:
                current.right = Node(data)
    
    def dfs(self, node):
        if node:
            self.dfs(node.left)
            print(node.data, end = " ")
            self.dfs(node.right)
    
    def bfs(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:    
            node = queue.pop(0)
            print(node.data, end = " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if node is None:
            return None
        elif node.data == data:
            return node
        elif node.data < data:
            return self._search(node.right, data)
        else:
            return self._search(node.left, data)
    
    def remove(self, data):
        self.root = self._remove(self.root, data)
        return self.root
    
    def _remove(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None 
            elif node. left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._min_value_node(node.right)
                node.data = successor.data
                node.right = self._remove(node.right, successor.data)
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# Create a tree
tree = Tree()

# Insert values
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

# Print the tree using DFS (In-Order)
print("DFS (In-Order):")
tree.dfs(tree.root)
print()

# Print the tree using BFS
print("BFS (Level Order):")
tree.bfs()
print()

# Search for a value
print("\nSearching for 40:")
result = tree.search(40)
print("Found" if result else "Not found")

# Remove a node
print("\nRemoving 30:")
tree.remove(30)
print("DFS after removal:")
tree.dfs(tree.root)
print()
