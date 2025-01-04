# 내장 함수 -> sum, min, max, eval, sorted,
result = sum([1,2,3,4,5])
print(result)

result = min([1,4,3,5])
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([1,4,3,5,6,2])
print(result)

result = sorted([1,4,3,5,6,2],reverse = True)
print(result)

#리스트의 원소로 튜플이 존재

result = sorted([('홍길동',35), ('이순신', 75), ('아무개', 50)], key = lambda x : x[1], reverse = True)
print(result)

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

# 순열 (3P3): ['A', 'B', 'C']로 만들 수 있는 순열 (3개의 원소로 이루어진 모든 순서쌍)
result = list(permutations(data, 3))  # 3P3
print(result)
# 결과: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합 (3C2): ['A', 'B', 'C']에서 순서와 관계없이 2개를 뽑는 조합
result = list(combinations(data, 2))  # 3C2
print(result)
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열: 각 원소를 중복하여 2개의 원소로 구성된 순열 (Cartesian Product)
result = list(product(data, repeat=2))  # 중복 순열
print(result)
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 중복 조합 (3H2): ['A', 'B', 'C']에서 중복을 허용하여 2개를 뽑는 조합
result = list(combinations_with_replacement(data, 2))  # 3H2
print("Combinations with Replacement (3H2):", result)
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]