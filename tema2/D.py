import sys

def f(x):
    return a * x * x * x + b * x * x + c * x + d


data = sys.stdin.read().split()
it = iter(data)
a = int(next(it))
b = int(next(it))
c = int(next(it))
d = int(next(it))

left = -10000.0
right = 10000.0

while right - left > 1e-5:
    mid = (left + right) / 2
    if f(left) * f(mid) <= 0:
        right = mid
    else:
        left = mid

print((left + right) / 2)
