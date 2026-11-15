import sys
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        curr = self.root
        while True:
            if key < curr.data:
                if curr.left is None:
                    curr.left = Node(key)
                    break
                curr = curr.left
            elif key > curr.data:
                if curr.right is None:
                    curr.right = Node(key)
                    break
                curr = curr.right
            else:
                break

    def size(self):
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)


    num = map(int, sys.stdin.read().split())
    bst = BinarySearchTree()
    for n in num:
        if n == 0:
            break
        bst.insert(n)
    print(bst.size())
