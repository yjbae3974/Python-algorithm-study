N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
max_num = max(arr)
dp = [0] * max_num
dp[0] = 1
dp[1] = 2
if max_num > 1:
    dp[2] = 4
if max_num > 2:
    for i in range(3, max_num):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
for num in arr:
    print(dp[num - 1])