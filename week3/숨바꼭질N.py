def distance(a,b):
    if a> b:
        return a-b
    else:
        return b-a
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
def gcd_n(arr):
    a = arr[0]
    for i in arr:
        a = gcd(i,a)
    return a

N, S = map(int, input().split())
arr = list(map(int, input().split()))

if(N == 1):
    print(distance(S,arr[0]))
else:
    for i in range(N):
        arr[i] = distance(arr[i], S)
    print(gcd_n(arr))

