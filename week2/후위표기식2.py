def replace_expression(expression, values):
    replace_dict = {chr(65 + i): values[i] for i in range(len(values))}

    result = []

    for char in expression:
        if char in replace_dict:
            result.append(replace_dict[char])
        else:
            result.append(char)
    return result


N = int(input())
expression = list(input().strip())
stk = []
values = [int(input()) for _ in range(N)]
result = replace_expression(expression, values)

for char in result:
    if isinstance(char, int):
        stk.append(char)
    else:
        temp2 = stk.pop()
        temp1 = stk.pop()
        if char == '+':
            stk.append(temp1 + temp2)
        elif char == '-':
            stk.append(temp1 - temp2)
        elif char == '/':
            stk.append(temp1 / temp2)
        elif char == '*':
            stk.append(temp1 * temp2)
print(f"{stk[0]:.2f}")
