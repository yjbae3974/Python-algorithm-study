def to_negabinary(n):
    if n == 0:
        return "0"

    result = []
    while n != 0:
        n, remainder = divmod(n, -2)
        if remainder < 0:
            remainder += 2
            n += 1
        result.append(str(remainder))

    return ''.join(result[::-1])


# 입력 받기
n = int(input())
print(to_negabinary(n))
