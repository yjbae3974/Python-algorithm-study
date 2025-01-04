import random

# 예시 데이터: (이름, 키)
data = [('banana', 2), ('apple', 2), ('orange', 1), ('kiwi', 2), ('grape', 3)]

# 데이터를 섞어서 불안정한 정렬에서 순서가 바뀔 수 있도록 함
random.shuffle(data)

print("Original data:")
print(data)

# Stable Sort: 병합 정렬 (Python 내장 sort())
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

stable_data = data[:]
print('Stable Sort 실행결과: ')
for _ in range(5):
    random.shuffle(stable_data)
    merge_sort(stable_data)
    print(stable_data)


# Unstable Sort: 퀵 정렬 (Quick Sort)
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j][1] < pivot[1]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


print("Unstable Sort 결과:")

for _ in range(5):
    random.shuffle(data)
    quick_sort(data, 0, len(data) - 1)
    print(data)

