import heapq

n = int(input())
cargo = []
for _ in range(n):
    t, l = map(int, input().split())
    cargo.append((t, l))
cargo.sort()
heap = []
max_apps = 0
for t, l in cargo:
    while heap and heap[0] <= t:
        heapq.heappop(heap)
    heapq.heappush(heap, t + l)
    if len(heap) > max_apps:
        max_apps = len(heap)
print(max_apps)
