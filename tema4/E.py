import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

total_cost = 0.0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    current_sum = a + b
    total_cost += current_sum * 0.05
    heapq.heappush(arr, current_sum)

print(f"{total_cost:.2f}")
