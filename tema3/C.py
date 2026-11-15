str = input().split()

stack = []
for civ in str:
    if not civ.isdigit():
        b = stack.pop()
        a = stack.pop()
        if civ == '+':
            res = a + b
        if civ == '-':
            res = a - b
        if civ == '*':
            res = a * b
        if civ == '/':
            res = a / b
        stack.append(res)
    else:
        stack.append(int(civ))
print(stack[0])
