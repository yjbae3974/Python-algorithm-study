def sieve_of_eratosthenes(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

def count_goldbach(n, is_prime):
    cnt = 0
    for i in range(2, n // 2 + 1):  # n//2까지 확인하면 충분
        if is_prime[i] and is_prime[n - i]:
            cnt += 1
    return cnt

N = int(input())
arr = [int(input()) for _ in range(N)]

limit = max(arr)
is_prime = sieve_of_eratosthenes(limit)

for num in arr:
    print(count_goldbach(num, is_prime))
