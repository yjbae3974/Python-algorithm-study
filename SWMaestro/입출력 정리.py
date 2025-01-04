import sys

#가장 전형적
N = int(input())

#각 데이터를 공백으로 구별하여 입력
data = list(map(int, input().split()))

# list가 아니라 각 변수에 받기
n,m,k = list(map(int,input().split()))

#빠른 input 받기
data = sys.stdin.readline().rstrip()