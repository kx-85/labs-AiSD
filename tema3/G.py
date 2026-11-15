stack =[]
n = int(input())
vag = list(map(int, input().split()))
k =1

for el in vag:
    stack.append(el)
    while stack and stack[-1] == k:
        stack.pop()
        k += 1

if n + 1 == k:
    print('YES')
else:
    print('NO')
