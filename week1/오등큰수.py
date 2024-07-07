N = int(input())
stk = []
counted_dict = {}
ans = [-1] * N
seq = []


stk = list(map(int, input().split()))
for num in stk:
    if num in counted_dict:
        counted_dict[num] += 1
    else:
        counted_dict[num] = 1
for i in reversed(range(N)):
    while len(seq) != 0 and counted_dict[seq[-1]] <= counted_dict[stk[i]]:
        seq.pop()
    if len(seq) == 0:
        ans[i] = -1
        seq.append(stk[i])
    else:
        ans[i] = seq[-1]
        seq.append(stk[i])
print(' '.join(map(str, ans)))