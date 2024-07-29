N,M=map(int,input().split())
arr = list(map(int, input().split()))

max_list = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] <= M:
                max_list.append(arr[i] + arr[j] + arr[k])
print(max(max_list))