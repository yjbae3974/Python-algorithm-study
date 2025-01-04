import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min = i
        print(f'Iteration {i+1}:')
        for j in range(i + 1, n):
            print(f'인덱스{j}인 {data[j]}와 인덱스{i}인 {data[i]}을 비교.')
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
        print(f'  Result after iteration {i+1}: {data}')
        print('-' * 50)

selection_sort(data)

print(f'정렬된 data: {data}')