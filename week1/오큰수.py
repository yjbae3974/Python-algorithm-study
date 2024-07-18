N = int(input())
stk = [] #이 곳에 주어진 수들이 들어감.
ans = [-1] * N # ans 리스트 초기화. default값은 -1.
seq = [] #스택 역할을 수행함.


stk = list(map(int, input().split()))

for i in reversed(range(N)): #리스트를 역순으로 순회. 오른쪽에 있는 수 중 가장 큰 수를 탐색하므로 이 방식이 가장 효육적.
    while len(seq) != 0 and seq[-1] <= stk[i]:
        # 스택에 값이 들어가 있고 스택의 가장 위에 있는 값이 현재 탐색중인 값보다 작을동안 반복.
        seq.pop()
    if len(seq) == 0:
        #만약 스택이 비어있으면, 현재 수보다 큰 값이 오른쪽에 없다는 뜻이므로 -1을 대입, 현재 값을 스택에 푸시.
        ans[i] = -1
        seq.append(stk[i])
    else:
        #스택이 비어있지 않다면, 스택의 가장 위의 값이 오큰수이므로 해당 값을 대입. 현재 값을 스택에 푸시.
        ans[i] = seq[-1]
        seq.append(stk[i])
print(' '.join(map(str, ans)))