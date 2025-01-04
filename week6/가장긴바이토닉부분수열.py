N = int(input())
arrs = list(map(int, input().split()))

dpup = [1] * N
dpdown = [1] * N

# Calculate dpup array
for i in range(N):
    for j in range(i):
        if arrs[i] > arrs[j]:
            dpup[i] = max(dpup[i], dpup[j] + 1)

# Calculate dpdown array
for i in range(N):
    for j in range(i):
        if arrs[N - 1 - i] > arrs[N - 1 - j]:
            dpdown[N - 1 - i] = max(dpdown[N - 1 - i], dpdown[N - 1 - j] + 1)

# Find all indices with maximum dpup value
max_up_value = max(dpup)
up_indices = [i for i, x in enumerate(dpup) if x == max_up_value]

# Find all indices with maximum dpdown value
max_down_value = max(dpdown)
down_indices = [i for i, x in enumerate(dpdown) if x == max_down_value]

# Calculate the longest bitonic subsequence length
max_length = 0
for up_index in up_indices:
    # Calculate using the up index
    if up_index + 1 < N:
        upfirst = dpup[up_index] + max(dpdown[up_index + 1:], default=0)
        max_length = max(max_length, upfirst)

for down_index in down_indices:
    # Calculate using the down index
    if down_index > 0:
        downfirst = dpdown[down_index] + max(dpup[0:down_index], default=0)
        max_length = max(max_length, downfirst)

print(max_length)
