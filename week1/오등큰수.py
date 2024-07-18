N = int(input())
stk = []
counted_dict = {}   #오큰수와 다른 점: 시간복잡도 O(N)을 사용하여 순회. dict를 완성. 수 비교를 dict끼리 비교.
ans = [-1] * N  #초기화. default값은 -1.
seq = []


stk = list(map(int, input().split()))
#오큰수와 로직은 동일. 다만 비교할 수는 dict를 통해 정의된 각 수가 출현한 횟수를 비교.
for num in stk:
    #순회로직. dict를 완성함.
    if num in counted_dict:
        counted_dict[num] += 1
    else:
        counted_dict[num] = 1
for i in reversed(range(N)):
    #오큰수와 동일한 로직. 역순으로 순회하며 오른쪽부터 시작. count dict끼리 비교하며 ans에는 stk값을 기입.
    while len(seq) != 0 and counted_dict[seq[-1]] <= counted_dict[stk[i]]:
        seq.pop()
    if len(seq) == 0:
        ans[i] = -1
        seq.append(stk[i])
    else:
        ans[i] = seq[-1]
        seq.append(stk[i])
print(' '.join(map(str, ans)))