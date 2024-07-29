num_dict = {i:1 for i in range(10)}
num_dict[0]=0
N = int(input())
for i in range(1,N):
    new_num_dict = {i:0 for i in range(10)}
    for j in range(10):
        if j == 0:
            new_num_dict[j+1] +=num_dict[j]
        elif j == 9:
            new_num_dict[j-1] += num_dict[j]
        else:
            new_num_dict[j - 1] += num_dict[j]
            new_num_dict[j + 1] += num_dict[j]
    num_dict.update(new_num_dict)
cnt = 0
for i in range(10):
    cnt += num_dict[i]
print(cnt % 1000000000)

