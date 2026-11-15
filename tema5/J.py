import sys

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.count = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        c = self.root
        while True:
            if key < c.data:
                if c.left is None:
                    c.left = Node(key)
                    break
                c = c.left
            elif key > c.data:
                if c.right is None:
                    c.right = Node(key)
                    break
                c = c.right
            else:
                c.count += 1
                break

    def print_freq(self):
        def order(node):
            if node is None:
                return
            order(node.left)
            print(node.data, node.count)
            order(node.right)
        order(self.root)


num = map(int, sys.stdin.read().split())
bst = BinarySearchTree()
for n in num:
    if n == 0:
        break
    bst.insert(n)
bst.print_freq()
