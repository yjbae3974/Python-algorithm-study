# N = int(input())
#
# n = int(N ** 0.5)
# arr = [0] * (n + 1)
# for i in range(1, n + 1):
#     arr[i] = i**2
# cnt = 0
# while N >= 1:
#     if(N >= arr[n] and n >= 1):
#         N -= arr[n]
#         cnt += 1
#     else:
#         if(n == 1):
#             cnt += 1
#             break
#         n -=1
# print(cnt)

def min_square_terms(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[N]

N = int(input().strip())
print(min_square_terms(N))