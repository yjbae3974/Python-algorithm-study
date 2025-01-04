import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def merge_sort(arr):
    print(f'merge_sort실행. list={arr}')
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    print(f'merge 실행. left={left}, right={right}')
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
    #위 두 코드는, 각 배열에서 아직 처리되지 않은 요소들을 모두 sorted_array에 추가하는 역할을 한다!
    print(f'sorted_array={sorted_array}')
    return sorted_array

data = merge_sort(data)

print(f'정렬된 data: {data}')