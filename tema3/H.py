from collections import deque
def balance():
    if len(l) < len(r):
        l.append(r.popleft())
    elif len(l) > len(r) + 1:
        r.appendleft(l.pop())


n = int(input())
l = deque()
r = deque()
out = []
for _ in range(n):
    cmd = input().split()
    cm = cmd[0]
    if cm == '+':
        r.append(int(cmd[1]))
        balance()
    elif cm == '*':
        l.append(int(cmd[1]))
        balance()
    elif cm == '-':
        out.append(str(l.popleft()))
        balance()
print('\n'.join(out))
