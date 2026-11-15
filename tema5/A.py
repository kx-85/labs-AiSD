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
            return "DONE"
        curr = self.root
        while True:
            if key < curr.data:
                if curr.left is None:
                    curr.left = Node(key)
                    return "DONE"
                curr = curr.left
            elif key > curr.data:
                if curr.right is None:
                    curr.right = Node(key)
                    return "DONE"
                curr = curr.right
            else:
                return "ALREADY"

    def search(self, key):
        curr = self.root
        while curr is not None:
            if key == curr.data:
                return "YES"
            elif key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return "NO"

    def delete(self, key):
        def find_max(node):
            while node.right is not None:
                node = node.right
            return node

        def _delete(node, key):
            if node is None:
                return None, "CANNOT"

            if key < node.data:
                node.left, status = _delete(node.left, key)
                return node, status
            elif key > node.data:
                node.right, status = _delete(node.right, key)
                return node, status
            else:
                if node.left is None:
                    return node.right, "DONE"
                elif node.right is None:
                    return node.left, "DONE"
                else:
                    max_node = find_max(node.left)
                    node.data = max_node.data
                    node.left, _ = _delete(node.left, max_node.data)
                    return node, "DONE"

        self.root, status = _delete(self.root, key)
        return status

    def print_(self):
        def _print(node, level):
            if node is None:
                return
            _print(node.left, level + 1)
            print("." * level + str(node.data))
            _print(node.right, level + 1)

        _print(self.root, 0)


    bst = BinarySearchTree()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0]
        if command == "ADD":
            n = int(parts[1])
            print(bst.insert(n))
        elif command == "DELETE":
            n = int(parts[1])
            print(bst.delete(n))
        elif command == "SEARCH":
            n = int(parts[1])
            print(bst.search(n))
        elif command == "PRINTTREE":
            bst.print_()
