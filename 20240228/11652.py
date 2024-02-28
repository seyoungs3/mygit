# 카드

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

cnt = 0
mxval = -2**62-1
mxcnt = 0

for i in range(n):
    if i == 0 or arr[i] == arr[i-1]:
        cnt += 1
    if arr[i] != arr[i-1]:
        cnt = 1
    if cnt > mxcnt:
        mxcnt = cnt
        mxval = arr[i]

print(mxval)
