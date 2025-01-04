#500, 100, 50, 10원이 무한히 존재. N원 거슬러줘야됨. 동전의 최소 개수. N은 항상 10의 배수

N = 1000 - int(input())
cnt = 0

for i in range(N, 499, -500):
    N -= 500
    cnt += 1
for i in range(N, 99, -100):
    N -= 100
    cnt += 1
for i in range(N, 49, -50):
    N -= 50
    cnt += 1
for i in range(N, 9, -10):
    N -= 10
    cnt += 1
for i in range(N, 4, -5):
    N -= 5
    cnt += 1
for i in range(N, 0, -1):
    N -= 1
    cnt += 1
print(cnt)