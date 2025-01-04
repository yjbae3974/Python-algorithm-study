#실수형

a = 5.
print(a)

a = -7.
print(a)

#10억

a = 1e9
print(a)

#752.7

a = 7.527e2
print(a)


#3.954
a = 39.54e-1
print(a)

# 리스트 자료형(크기가 N인 리스트로 초기화하기)

N = 10
a = [0] * N
print(a)


#접근법

for i in range(10):
    a[i]=i
print(a)
print(a[-1])
print(a[-3])


#리스트 빠르게 초기화

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1,10)]
print(array)

# N * M 크기의 2차원 리스트를 초기화할 때는 다음과 같이 사용한다. 참고로 반드시 이러한 형태를 써야 한다.

N = 3
M = 4

array = [[0] * M for i in range(N)]
print(array)

# 리스트 관련 method

# append
# sort
# sort(reverse = True)
# reverse
# insert(삽입할 위치 인덱스, 삽입할 값) 시간 복잡도가 N이므로 남발하지 말자
# count(특정 값) : 리스트 내에서 특정값을 가지는 데이터의 개수
# remove(특정 값): 특정한 값을 가진 원소를 제거. 값을 가진 원소가 여러개면 하나만 제거. 시간 복잡도가 N이다.

b = [1,1,2,3,1,2]
b.remove(1)
print(b) # 가장 작은 인덱스에 있는 것을 제거

#특정 값을 가지는 모든 원소 제거
# 아이디어: remove set을 만들고, 거기에 포함되어있지 않다면 추가. 시간 복잡도 그리 안큼
a = [1,2,3,4,5,5,5]
remove_set = {3,5} # set을 사용한다!
result = [i for i in a if a not in remove_set]
print(result)