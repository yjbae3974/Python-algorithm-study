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
        if left[i] > right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

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
            while j >= 0 and a[j] < tmp:
                a[j+h] = a[j]
                j -= h
            a[j + h] = tmp
            print(f'현재 배열상태: {a}')
        h //= 3

def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left + right) // 2]
    while pl <= pr:
        while a[pl] > x:
            pl += 1
        while a[pr] < x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left > pr: qsort(a,left,pr)
    if right < pl: qsort(a,pl,right)


input_data = input()
arr = [char for char in input_data]
arr_merge = arr
arr_shell = arr
arr_quick = arr
shell_sort(arr_shell)
qsort(arr_quick, 0, len(arr_shell) - 1)
print(''.join(merge_sort(arr_merge)))
print(''.join(arr_shell))
print(''.join(arr_quick))
