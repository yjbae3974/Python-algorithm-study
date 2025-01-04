def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0부터 9까지의 자릿수에 대해 카운트 배열 생성

    # 주어진 자릿수에 대해 count 배열에 각 숫자의 출현 횟수 기록
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 누적합 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 출력 배열을 위해 입력 배열을 역순으로 순회하며 각 요소의 위치를 계산
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 출력 배열을 원래 배열에 복사하여 현재 자릿수 기준으로 정렬된 배열을 만듦
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 가장 큰 숫자를 찾음
    max_val = max(arr)

    # 자릿수 별로 counting_sort를 수행
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 사용 예시
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("정렬된 배열:", arr)
