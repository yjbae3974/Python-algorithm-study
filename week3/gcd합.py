import sys

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
def gcd_sum(arr):
    sum_gcd = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            sum_gcd += gcd(arr[i], arr[j])
    return sum_gcd

input = sys.stdin.read
data = input().strip().split()
index = 0

t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + n]))
    index += n
    results.append(gcd_sum(arr))

for result in results:
    print(result)
