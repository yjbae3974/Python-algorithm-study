def findNum(a,b):
    if a>b:
        return b
    else:
        return a

a, b= input().split()
a = int(a)
b = int(b)
left = 1
index=2
while True:
    if a%index == 0 and b%index == 0:
        a //= index
        b //= index
        left *= index
        continue
    if findNum(a,b) > index:
        index += 1
        continue
    break
min = left
max = left * a * b
print(min)
print(max)