import random

N = int(input('원소 수를 입력하세요: '))

data = [random.randrange(1, 100) for _ in range(N)]
print(f'원래 data: {data}')

def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # 가장 큰 값을 찾기
    max_val = max(arr)

    # 도수 배열 생성 및 초기화
    count = [0] * (max_val + 1)

    # 도수 배열에 각 요소의 개수 저장
    for num in arr:
        count[num] += 1

    # 정렬된 배열 생성
    sorted_arr = []
    for num, cnt in enumerate(count):
        sorted_arr.extend([num] * cnt)

    return sorted_arr


sorted_arr = counting_sort(data)
print(sorted_arr)
