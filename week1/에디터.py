#스택 2개 이용.
import sys

sys_input = sys.stdin.read

commands = sys_input().strip().split('\n')
cursorL = list(commands[0])
cursorR = []

N = int(commands[1])
new_commands = commands[2:N+2]
for command in new_commands:
    if command[0] == 'L':
        if len(cursorL) != 0:
            cursorR.append(cursorL.pop())
    elif command[0] == 'D':
        if len(cursorR) != 0:
            cursorL.append(cursorR.pop())
    elif command[0] == 'B':
        if len(cursorL) != 0:
            cursorL.pop()
    elif command[0] == 'P':
        cursorL.append(command[2])

print(''.join(cursorL + cursorR[::-1]))
