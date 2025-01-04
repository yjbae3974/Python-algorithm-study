import random

def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left + right) // 2]
    print(f'pivot x : {x}')
    print(f'a[{left}] ~ a[{right}] :', *a[left:right+1])
    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    print(f'sorted: {a}')
    if left < pr: qsort(a,left,pr)
    if right > pl: qsort(a,pl,right)

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

qsort(data,0,N-1)
print(data)