word = input()
dict_list = {chr(ord('a') + i): word.find(chr(ord('a') + i)) for i in range(26)}
result = [str(dict_list[chr(ord('a') + i)]) for i in range(26)]
print(' '.join(result))