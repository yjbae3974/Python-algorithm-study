from collections import deque
N, K = map(int, input().strip().split(' '))
queue = deque()
arr = []
for i in range(1,N + 1):
    queue.append(i)
for _ in range(N):
    for _ in range(K - 1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())
print('<' + ', '.join(map(str, arr)) + '>')