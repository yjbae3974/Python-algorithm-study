import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 9:
	    h = h * 3 + 1
    while h > 0:
        print(f'현재 h값: {h}')
        for i in range(h,n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j + h] = tmp
            print(f'현재 배열상태: {a}')
        h //= 3

shell_sort(data)

print(f'정렬된 data: {data}')