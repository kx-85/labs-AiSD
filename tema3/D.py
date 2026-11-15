class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return 'ok'

    def is_Empty(self):
        return self.items == []

    def pop(self):
        if self.is_Empty():
            return "error"
        return self.items.pop(0)

    def front(self):
        if self.is_Empty():
            return "error"
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

qu = Queue()
while True:
    cmd = input().split()
    cm = cmd[0]
    if cm=='pop':
        print(qu.pop())
    elif cm=='front':
        print(qu.front())
    elif cm=='size':
        print(qu.size())
    elif cm=='clear':
        print(qu.clear())
    elif cm=='exit':
        print('bye')
        break
    elif cm=='push':
        print(qu.push(cmd[1]))
