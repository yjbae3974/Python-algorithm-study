import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(N)]

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 9:
	    h = h * 3 + 1
    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3
def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left + right) // 2]
    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr: qsort(a,left,pr)
    if right > pl: qsort(a,pl,right)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

#bubble_sort(arr)
#selection_sort(arr)
#shell_sort(arr)
#qsort(arr,0,N-1)
data = merge_sort(arr)
for i in range(N):
    print(data[i])