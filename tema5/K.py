import sys
input = sys.stdin.readline
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        cur = self.root
        while True:
            if x == cur.data:
                return
            elif x < cur.data:
                if cur.left is None:
                    cur.left = Node(x)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(x)
                    return
                cur = cur.right

    def next(self, x):
        cur = self.root
        ans = -1
        while cur is not None:
            if cur.data >= x:
                ans = cur.data
                cur = cur.left
            else:
                cur = cur.right
        return ans


n = int(input())
bst = BinarySearchTree()
after_query = False
last = -1
out = []
for _ in range(n):
    op, num = input().split()
    num = int(num)
    if op == '+':
        if after_query:
            num = (num + last) % 10 ** 9
        bst.add(num)
        after_query = False
    else:
        last = bst.next(num)
        out.append(last)
        after_query = True
print("\n".join(map(str, out)))
