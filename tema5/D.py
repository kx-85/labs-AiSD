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
                break

    def find_second_max(self):
        global parent_max

        def find_max(node):
            while node.right is not None:
                node = node.right
            return node
        c = self.root
        while c is not None:
            if c.right is None:
                if c.left is not None:
                    return find_max(c.left).data
                return parent_max.data
            parent_max = c
            c = c.right
        return None


    num = map(int, sys.stdin.read().split())
    bst = BinarySearchTree()
    for n in num:
        if n == 0:
            break
        bst.insert(n)
    print(bst.find_second_max())
