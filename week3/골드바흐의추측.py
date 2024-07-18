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

def find_goldbach(n, is_prime):
    for a in range(3, n // 2 + 1, 2):
        b = n - a
        if is_prime[a] and is_prime[b]:
            return a, b
    return None, None

import sys
sys_input = sys.stdin.read
data = sys_input().strip().split()

nums = [int(x) for x in data if int(x) != 0]
limit = max(nums)
is_prime = sieve_of_eratosthenes(limit)

for num in nums:
    a, b = find_goldbach(num, is_prime)
    if a is None or b is None:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{num} = {a} + {b}")
