s = input()
stack = []
ans = True

for civ in s:
    if civ not in ['(','{','[',')','}',']']:
        continue
    if civ in ['(','{','[']:
        stack.append(civ)
        continue
    if len(stack) != 0 and (civ == ')' and stack[-1] == '(' or civ == ']' and stack[-1] == '[' or civ == '}' and stack[-1] == '{'):
        stack.pop()
    else:
        ans = False
        break
if len(stack) != 0:
    ans = False
print('yes' if ans else 'no')
