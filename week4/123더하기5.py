import sys
input = sys.stdin.read
data = input().split()

#main알고리즘은 모두 짰으나 입력에서의 문제로 시간초과 뜸. 결국 입력부분만 gpt의 도움을 받아 다행히 시간초과 없이 해결..!
#이렇게 sys를 이용해서 받는게 가장 빠르다고 하네요! 참..

N = int(data[0])
nums = [int(data[i]) for i in range(1, N + 1)]
max_num = max(nums)

dp = [[0, 0, 0] for _ in range(max_num + 1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, max_num + 1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

results = []
for num in nums:
    X = (dp[num][0] + dp[num][1] + dp[num][2]) % 1000000009
    results.append(X)

sys.stdout.write('\n'.join(map(str, results)) + '\n')
