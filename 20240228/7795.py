# 먹을 것인가 먹힐 것인가

# 자기보다 크기가 작은 먹이만 먹을 수 있음
# 쌍의 갯수 구하기

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt = 0
    for aa in a:
        for bb in b:
            if aa > bb:
                cnt += 1
    print(cnt)