import sys
input = sys.stdin.read
data = input().split()

#아마 dp문제중 가장 어려운 문제. 많은 고민이 필요한 문제였고, 어떤 점화식을 써야하는지 결국 블로그의 도움을 빌렸다..!
#이번 문제는 입력을 받는 것도 어렵다. 시간제한 때문에 입력에서 최대한 시간을 쓰지 않기 위해 sys를 썼다.

#반례주의!
#col이 1인 경우를 고려하지 못해 99%에서 틀렸다고 떴다. 혹시 틀렸다고 뜬다면 위 경우를 계산하지 못했을 경우일 확률이 있다.


#알고리즘 설명
#뗀 스티커의 상하좌우가 다 찢어지므로, 이전 스티커의 대각선 위, 혹은 대각선 아래만 사용 가능하다.
#단, 고려해야할 건 바로 이전에 어떤 row를 선택했는지 만은 아니다. 그 전전 col에서 어떤 row를 선택했는지도 중요하다.
#따라서, 이전 대각선 위, 혹은 대각선 아래, 혹은 더더욱 이전 대각선 위, 대각선 아래를 고려하여 계속 합을 업데이트 해나가야 한다.

N = int(data[0])
ptr = 1
for _ in range(N):
    col = int(data[ptr])
    ptr += 1
    max_num = 0
    arr = [[0] * (col + 1) for _ in range(2)]
    for i in range(2):
        for j in range(1, col + 1):
            arr[i][j] = int(data[ptr])
            ptr += 1
    if(col > 1):
        for i in range(2, col + 1):
            arr[0][i] = arr[0][i] + max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] = arr[1][i] + max(arr[0][i - 1], arr[0][i - 2])
            max_num = max(max_num, arr[0][i], arr[1][i])
    else:
        max_num = max(arr[0][1], arr[1][1])
    print(max_num)