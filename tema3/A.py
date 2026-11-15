class Stack:
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
        return self.items.pop()

    def back(self):
        if self.is_Empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

st = Stack()
while True:
    cmd = input().split()
    cm = cmd[0]
    if cm=='pop':
        print(st.pop())
    elif cm=='back':
        print(st.back())
    elif cm=='size':
        print(st.size())
    elif cm=='clear':
        print(st.clear())
    elif cm=='exit':
        print('bye')
        break
    elif cm=='push':
        print(st.push(cmd[1]))
