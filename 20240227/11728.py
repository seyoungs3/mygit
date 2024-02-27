# 배열 합치기

# merge sort

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

aidx = 0
bidx = 0
c = []

for i in range(n+m):
    if aidx >= n:
        c.append(b[bidx])
        bidx+=1
    elif bidx >= m:
        c.append(a[aidx])
        aidx+=1
    elif a[aidx] <= b[bidx]:
        c.append(a[aidx])
        aidx+=1
    elif a[aidx] > b[bidx]:
        c.append(b[bidx])
        bidx+=1

print(*c)
    