def replace_expression(expression, values):
    #주어진 문자열에 있는 대문자 알파벳을 주어진 식으로 대체! 딕셔너리 이용
    replace_dict = {chr(65 + i): values[i] for i in range(len(values))}

    result = []

    for char in expression:
        if char in replace_dict:
            result.append(replace_dict[char])
        else:
            result.append(char)
    return result


N = int(input())
expression = list(input().strip())  #받은 문자열을 리스트로 분해.
stk = []
values = [int(input()) for _ in range(N)]#대체할 값들을 리스트 형식으로 받음.
result = replace_expression(expression, values)
#result는 알파벳이 숫자로 대체된 리스트임.
for char in result:
    #후위표기식을 계산하는 로직. 컴퓨터에 최적화된 계산식인 만큼 알고리즘도 간단.
    if isinstance(char, int):
        stk.append(char)
    else:
        temp2 = stk.pop()
        temp1 = stk.pop()
        if char == '+':
            stk.append(temp1 + temp2)
        elif char == '-':
            stk.append(temp1 - temp2)
        elif char == '/':
            stk.append(temp1 / temp2)
        elif char == '*':
            stk.append(temp1 * temp2)
print(f"{stk[0]:.2f}")
