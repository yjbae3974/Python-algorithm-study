N = int(input())

fib = [0] * N
fib[1] = 1

for i in range(2, N):
    fib[i] = fib[i - 1] + fib[i - 2]
print(fib)

