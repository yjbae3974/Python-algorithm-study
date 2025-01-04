def base_conversion2(A, B):
    string = []
    while A > 0:
        A,n = divmod(A, B)
        string.append(n)
    return string[::-1]

string, B = input().split()
string = int(string)
B = int(B)
ans = base_conversion2(string, B)
for num in ans:
    if num >= 10:
        print(chr(num + 55), end='')
    else:
        print(num, end='')


