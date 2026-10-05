def countingsort(arr):
    k = max(arr)
    counter = [0] * (k + 1)
    for x in arr:
        counter[x] += 1
    arr[:] = []
    for num in range(k + 1):
        arr += [num] * counter[num]


a = list(map(int,input().split()))
countingsort(a)
print(*a)
