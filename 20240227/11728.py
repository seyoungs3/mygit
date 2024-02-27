# 배열 합치기

# merge sort로 안했음

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b

c = sorted(c)

print(*c)