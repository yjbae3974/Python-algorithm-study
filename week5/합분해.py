N, K = map(int, input().split())

num_set = [[1] * N for i in range(K)]

for i in range(1, K+1):
    num_set[i-1][0] = i
for i in range(1,K):
    for j in range(1,N):
        num_set[i][j] = (num_set[i-1][j] + num_set[i][j-1]) % 1000000000
print(num_set[K-1][N-1])
