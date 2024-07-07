N = int(input())
stk = []
ans = [-1] * N
seq = []


stk = list(map(int, input().split()))
for i in reversed(range(N)):
    while len(seq) != 0 and seq[-1] <= stk[i]:
        seq.pop()
    if len(seq) == 0:
        ans[i] = -1
        seq.append(stk[i])
    else:
        ans[i] = seq[-1]
        seq.append(stk[i])
print(' '.join(map(str, ans)))