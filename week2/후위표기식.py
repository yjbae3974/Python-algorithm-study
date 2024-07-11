midfix = list(input())
stk = []
result = []
priority = {'*': 2, '/': 2, '+': 1, '-': 1}


for char in midfix:
    if char == '(':
        stk.append(char)
    elif 'A' <= char <= 'Z':
        result.append(char)
    elif char == ')':
        while stk and stk[-1] != '(':
            result.append(stk.pop())
        stk.pop()
    else:
        while stk and stk[-1] in priority and priority[char] <= priority[stk[-1]]:
            result.append(stk.pop())
        stk.append(char)

while stk:
    result.append(stk.pop())

print(''.join(result))
