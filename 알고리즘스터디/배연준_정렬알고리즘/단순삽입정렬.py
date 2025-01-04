"""
종료조건: 정렬된 배열의 왼쪽 끝에 도달한 경우
종료조건: tmp보다 작거나 키값이 같은 원소를 발견할 경우
"""
"""
드모르간 법칙 적용:
계속조건: j가 0보다 큰 경우
계속조건: a[j-1]의 값이 tmp보다 큰 경우
"""

import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        print(f'{i}번째 값인 {a[i]}와 {j-1}번째 값인 {a[j-1]}인 값을 비교.')
        while j > 0 and a[j - 1] > tmp:
            print(f'{j}번째 값인 {a[j]}을 {j - 1}번째로 이동.')
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
        print(f'  Result after iteration {i + 1}: {data}')
        print('-' * 50)

insertion_sort(data)

print(f'정렬된 data: {data}')