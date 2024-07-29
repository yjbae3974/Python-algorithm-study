def base_conversion(arr, A):
    dim_10 = 0
    for i, num in enumerate(reversed(arr)):
        dim_10 += num * (A ** i)
    return dim_10


string, B = input().split()
dim = []
for char in string:
    if char.isalpha():
        dim.append(ord(char) - ord('A') + 10)
    else:
        dim.append(ord(char) - ord('1') + 1)

print(base_conversion(dim, int(B)))
