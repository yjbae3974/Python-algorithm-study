N, S = map(int, input().split())
arr = list(map(int, input().split()))
count_len = []
count = 0
interval_sum = 0
end = 0
impossible = 0
# start를 차례대로 증가시키며 반복
for start in range(N):
    # end만큼 이동시키기
    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum >= S:
        impossible += 1
        count += 1
        count_len.append(end - start)
    interval_sum -= arr[start]
if(impossible == 0):
    print(0)
else:
    print(min(count_len))
