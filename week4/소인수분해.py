def factorization(a,n):
    while a % n == 0:
        print(n)
        a = a//n
    return a

N = int(input())
for i in range(2, N + 1):
    N = factorization(N,i)