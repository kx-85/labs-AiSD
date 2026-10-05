import sys

data = sys.stdin.read().split()
it = iter(data)
c = float(next(it))

left = 0.0
right = c
while right - left > 1e-7:
    mid = (left + right) / 2
    if mid * mid + mid ** 0.5 < c:
        left = mid
    else:
        right = mid

print((left + right) / 2)
