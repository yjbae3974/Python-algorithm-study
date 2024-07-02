stack = []
operations = []
arr = []
N = int(input())

for i in range(N):
    arr.append(input())

num = 1
is_possible = True

for value in arr:
    while num <= int(value):
        stack.append(num)
        num += 1
        operations.append('+')
    if stack and stack[-1] == int(value):
        stack.pop()
        operations.append('-')
    else:
        is_possible = False
        break
if is_possible:
    for operation in operations:
        print(operation)
else:
    print('NO')