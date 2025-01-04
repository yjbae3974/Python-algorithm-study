num_dict = {i:1 for i in range(10)}
num_dict[0]=1
N = int(input())
for i in range(1,N):
    new_num_dict = {i:0 for i in range(10)}
    for j in range(10):
        for k in range(10 - j):
            new_num_dict[j + k] += num_dict[j]

    num_dict.update(new_num_dict)
cnt = 0
for i in range(10):
    cnt += num_dict[i]
print(cnt % 10007)

