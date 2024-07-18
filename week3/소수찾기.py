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

N = int(input())
arr = list(map(int, input().split()))
limit = max(arr)
is_prime = sieve_of_eratosthenes(limit)
cnt = 0
for num in arr:
    if is_prime[num]:
        cnt += 1
print(cnt)