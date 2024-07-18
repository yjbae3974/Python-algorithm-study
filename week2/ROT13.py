def rot13(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char

input_str = input()
output_str = ''.join(rot13(char) for char in input_str)
print(output_str)
