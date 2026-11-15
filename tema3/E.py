class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items = [item] + self.items
        return 'ok'

    def push_back(self, item):
        self.items.append(item)
        return 'ok'

    def pop_front(self):
        if self.is_Empty():
            return 'error'
        return self.items.pop(0)

    def pop_back(self):
        if self.is_Empty():
            return 'error'
        return self.items.pop()

    def is_Empty(self):
        return self.items == []

    def front(self):
        if self.is_Empty():
            return "error"
        return self.items[0]

    def back(self):
        if self.is_Empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

dq = Deque()
while True:
    cmd = input().split()
    cm = cmd[0]
    if cm=='pop_front':
        print(dq.pop_front())
    elif cm=='pop_back':
        print(dq.pop_back())
    elif cm=='front':
        print(dq.front())
    elif cm=='back':
        print(dq.back())
    elif cm=='size':
        print(dq.size())
    elif cm=='clear':
        print(dq.clear())
    elif cm=='exit':
        print('bye')
        break
    elif cm=='push_front':
        print(dq.push_front(cmd[1]))
    elif cm=='push_back':
        print(dq.push_back(cmd[1]))
