N = int(input())

arr = [0] * (N + 1)
if(N>=2):
    arr[2] = 1
for i in range(3, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        arr[i] = min(arr[i//2], arr[i//3], arr[i-1]) + 1
    elif i % 3 == 0 and i % 2 != 0:
        arr[i] = min(arr[i//3], arr[i-1]) + 1
    elif i % 2 == 0 and i % 3 != 0:
        arr[i] = min(arr[i//2], arr[i-1]) + 1
    else:
        arr[i] = arr[i-1] + 1
print(arr[N])