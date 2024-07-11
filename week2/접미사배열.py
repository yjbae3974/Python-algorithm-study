str_list = []
word = input()
suffixes = [word[i:] for i in range(len(word))]
suffixes.sort()
for suffix in suffixes:
    print(suffix)