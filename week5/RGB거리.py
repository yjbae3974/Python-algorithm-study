import sys
input = sys.stdin.read
data = input().split()

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

N = int(data[0])
ptr = 1
RGB = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    for j in range(3):
        RGB[i][j] = int(data[ptr])
        ptr += 1
for i in range(1, N):
    RGB[i][0] = min(RGB[i-1][1],RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0],RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0],RGB[i-1][1]) + RGB[i][2]

print(min(RGB[N-1]))



