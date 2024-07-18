import math

def count_factor(a,b):
    count = 0
    while a >= b:
        count += a // b
        a //= b
    return count

n,m=map(int,input().split())
count_two_of_n = count_factor(n,2)
count_five_of_n = count_factor(n,5)
count_two_of_m = count_factor(m,2)
count_five_of_m = count_factor(m,5)
count_two_of_nm = count_factor(n-m,2)
count_five_of_nm = count_factor(n-m,5)
tot_two = count_two_of_n - count_two_of_m - count_two_of_nm
tot_five = count_five_of_n - count_five_of_m - count_five_of_nm
cnt_ten = min(tot_two,tot_five)
print(cnt_ten)