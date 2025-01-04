#최댓값을 먼저 구하고,

N = int(input())
arrs = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if arrs[i] > arrs[j]:
            dp[i] = max(dp[i], dp[j] + 1)
result = []
max_dp = max(dp)
print(max_dp)
for i in range(N-1,-1,-1):
    if dp[i] == max_dp:
        result.append(arrs[i])
        max_dp -= 1
print(*result[::-1])
