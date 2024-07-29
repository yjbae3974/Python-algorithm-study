def base_conversion(arr, A, m):
    dim_10 = 0
    for i, num in enumerate(reversed(arr)):
        dim_10 += num * (A ** i)
    return dim_10

def base_conversion2(A, B):
    string = []
    #A: 10진법으로 변환된 수.
    #B: 변환하기를 원하는 N진법.
    while A > 0:
        A,n = divmod(A, B)
        string.append(n)
    return string[::-1]


A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
dim_10 = base_conversion(arr, A, m)
list_int = base_conversion2(dim_10, B)
print(' '.join(map(str,list_int)))
