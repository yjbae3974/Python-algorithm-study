word = input()
dict_list = {chr(ord('a') + i): word.count(chr(ord('a') + i)) for i in range(26)}
for value in dict_list.values():
    print(value,end=' ')