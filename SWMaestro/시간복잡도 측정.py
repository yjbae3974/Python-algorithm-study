from random import randint
import time

#배열에 10000개 정수 삽입

array = []
for _ in range(10000):
    array.append(randint(0, 100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            array[min_index] , array[j] = array[j], array[min_index]
end_time = time.time()
print("선택 정렬 성능 측정:", end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))
start_time = time.time()
array.sort()
end_time = time.time()
print("기본 정렬 성능 측정:", end_time - start_time)

