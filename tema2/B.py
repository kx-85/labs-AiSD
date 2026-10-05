import sys

data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
k = int(next(it))
m1 = [int(next(it)) for _ in range(n)]
m2 = [int(next(it)) for _ in range(k)]

for i in m2:
    left = -1
    right = len(m1)
    while right - left > 1:
        ser = (left+right)//2
        if m1[ser] <= i:
            left = ser
        else:
            right = ser
    if left +1 < len(m1):
        if abs(i - m1[left]) <= abs(i - m1[left+1]):
            print(m1[left])
        else:
            print(m1[left+1])
    else:
        print(m1[left])
