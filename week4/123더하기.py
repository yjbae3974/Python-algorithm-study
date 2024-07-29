import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
nums = [int(data[i]) for i in range(1, N + 1)]
max_num = max(nums)

dp = [0 for i in range(max_num + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
if(max_num > 4):
    for i in range(4, max_num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for num in nums:
    print(dp[num])

