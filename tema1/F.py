import sys
from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    val = arr[randint(0, len(arr) - 1)]
    left, center, right = [], [], []
    for x in arr:
        if x < val:
            left.append(x)
        elif x > val:
            right.append(x)
        else:
            center.append(x)
    return quick_sort(left) + center + quick_sort(right)


inp_d = sys.stdin.read().split()
n = int(inp_d[0])
a = [int(i) for i in inp_d[1:n+1]]
print(*quick_sort(a))
