N = int(input())

cost = [0] * N
dp0 = [0] * N
dp1 = [0] * N
dp2 = [0] * N

for i in range(N):
    cost[i] = int(input())
dp1[0] = cost[0]
for i in range(1, N):
        dp0[i] = max(dp0[i-1], dp1[i - 1], dp2[i - 1])
        dp1[i] = dp0[i - 1] + cost[i]
        dp2[i] = dp1[i - 1] + cost[i]
print(max(dp0[N-1], dp1[N-1], dp2[N-1]))

