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

    def check_bal(self):
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            if lh == -1:
                return -1
            rh = height(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return height(self.root) != -1


num = map(int, sys.stdin.read().split())
bst = BinarySearchTree()
for n in num:
    if n == 0:
        break
    bst.insert(n)
if bst.check_bal():
    print("YES")
else:
    print("NO")
