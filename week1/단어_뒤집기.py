T = int(input().strip())

for _ in range(T):
    line = input().strip()
    words = line.split()
    reversed_words = [word[::-1] for word in words]
    print(' '.join(reversed_words))


