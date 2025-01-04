import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        print(f'Iteration {i+1}:')
        for j in range(n - 1, i, -1):
            print(f'인덱스{j}인 {data[j]}와 인덱스{j-1}인 {data[j-1]}을 비교.')
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            print(f'  Step {n-1-j+1}: {data}')
        print(f'  Result after iteration {i+1}: {data}')
        print('-' * 50)

bubble_sort(data)

print(f'정렬된 data: {data}')
