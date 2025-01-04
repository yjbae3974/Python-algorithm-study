N = int(input())
if N != 1:
    dp = [0 for _ in range(N + 1)]
    dp[1] = 1
    dp[2] = 3
    if N > 2:
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2] * 2
    print(dp[N] % 10007)
else:
    print(1)