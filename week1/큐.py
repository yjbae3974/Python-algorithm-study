from collections import deque
import sys

sys_input = sys.stdin.read
data = sys_input().strip().split('\n')

N = int(data[0])
commands = data[1:N + 1]

queue = deque()

for command in commands:
    command = command.split(' ')
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

