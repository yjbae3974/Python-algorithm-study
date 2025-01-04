N = int(input())
arr = list(map(int, input().split()))
dp = [10000 for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+arr[j-1])
print(dp[N])