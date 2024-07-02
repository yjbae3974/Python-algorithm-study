import re
def split_string(input_string):
    pattern = r'(<.*?>|\s|[^<\s]+)'

    # 위 정규표현식에 대한 설명:
    # <.*?>: <로 시작, >로 끝나는 문자열.
    # \s: 공백 문자.
    # [^<\s]+: <혹은 공백(\s)이 아닌 연속된 문자.


    result = re.findall(pattern, input_string)
    return result

input_string = input()

result = split_string(input_string)
reversed = []
for word in result:
    if '<' in word or '>' in word:
        reversed.append(word)
        continue
    else:
        word = word[::-1]
    reversed.append(word)
print(''.join(reversed))
