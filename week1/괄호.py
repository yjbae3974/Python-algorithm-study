T = int(input())

for i in range(T):
    cnt = 0
    if_pass = False
    l = list(input())
    for j in range(len(l)):
        if l[j] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            if_pass = True
            break
    if(if_pass == False):
        if cnt == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


