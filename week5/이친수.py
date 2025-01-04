N = int(input())

dp1 = [0] * N
dp0 = [0] * N
dp1[0] = 1
if N > 1:
    dp0[1] = 1
for i in range(2, N):
    dp1[i] = dp0[i-1]
    dp0[i] = dp0[i-1] + dp1[i-1]
print(dp0[N-1] + dp1[N-1])

