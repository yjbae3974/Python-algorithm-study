import sys

class Stack:
    def __init__(self):
        self.stack = []

    def default(self):
        print(self)
        print(self.stack)
        return -1

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if len(self.stack) == 0 else 0

    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

# 여러 줄의 입력을 받음 (종료 조건으로 빈 줄 사용)
commands = []
while True:
    try:
        line = input().strip()
        if line == "":
            break
        commands.append(line)
    except EOFError:
        break

n = int(commands[0])
stack = Stack()
result = []

for i in range(1, n + 1):
    command = commands[i].split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        result.append(stack.pop())
    elif command[0] == 'size':
        result.append(stack.size())
    elif command[0] == 'empty':
        result.append(stack.empty())
    elif command[0] == 'top':
        result.append(stack.top())
    else:
        result.append(stack.default())

for res in result:
    print(res)
