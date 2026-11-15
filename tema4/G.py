import heapq

n = int(input())
a = [int(input()) for _ in range(n)]
heap = []
for i in range(n):
    t = max(1000 - a[i], 1)
    heapq.heappush(heap, (t, i))
pos = 0
last_time = 0
while heap:
    t, idx = heapq.heappop(heap)

    if last_time + abs(pos - idx) <= t:
        last_time = t
        pos = idx
        a[idx] += 1
        next_t = max(1000 - a[idx], 1)
        heapq.heappush(heap, (t + next_t, idx))
    else:
        print(t)
        break
