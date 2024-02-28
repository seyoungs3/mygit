# 수 정렬하기 5

# 절댓값이 1000000보다 작거나 같은 정수

import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(2000001)]
for _ in range(n):
    num = int(input())
    arr[num+1000000] += 1

for i in range(2000001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i-1000000)