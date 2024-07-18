import math

def count_factor(a,b):
    count = 0
    while a >= b:
        count += a // b
        a //= b
    return count

n = int(input())
count_two_of_n = count_factor(n,2)
count_five_of_n = count_factor(n,5)

cnt_ten = min(count_two_of_n,count_five_of_n)
print(cnt_ten)