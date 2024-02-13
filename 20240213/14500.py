# 테트로미노
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노, 5종류
# n*m 종이 위에 테트로미노를 하나 놓음
# 테트로미노가 놓인 칸에 쓰여 있는 수의 합을 최대로
# 테트로미노 회전이나 대칭 가능

# bfs
# area == 4

# cheated
#  ㅓ ㅏ ㅗ ㅜ 모양 구현 잘 이해 못했음 -> 34, 35줄
# 시간초과

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(i,j, cnt):
    global mx, sum
    if cnt == 4:
        mx = max(mx, sum)
        return
    for dir in range(4):
        x = i+dx[dir]
        y = j+dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if vis[x][y] != 0:
            continue
        sum += scores[x][y]
        vis[x][y] = 1
        bfs(x,y,cnt+1) # 새로운 칸에서 탐색
        if cnt == 2:
            bfs(i,j,cnt+1) # 이전 칸에서 탐색
        sum -= scores[x][y]
        vis[x][y] = 0

n, m = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]
mx = 0
for i in range(n):
    for j in range(m):
        sum = scores[i][j]
        vis[i][j] = 1
        bfs(i,j,1)
        vis[i][j] = 0

print(mx)