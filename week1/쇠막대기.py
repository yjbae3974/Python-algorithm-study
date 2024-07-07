stack = []

input_line = list(input())
prev = '('
cnt = 0
for index, char in enumerate(input_line):
    if index == 0 and char == '(':
        stack.append(char)
        prev = char
        continue
    if char == '(':
        prev = char
        stack.append(char)
    else:
        if prev == '(':
            stack.pop()
            if(len(stack) != 0):
                prev = char
                cnt += len(stack)

        else:
            cnt += 1
            prev = char
            stack.pop()
print(cnt)
