from collections import deque
import sys

sys_input = sys.stdin.read
data = sys_input().strip().split('\n')

dq = deque()

N = int(data[0])
commands = data[1:N + 1]

for command in commands:
    command = command.split(' ')
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
