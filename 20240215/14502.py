# 연구소

# 벽을 꼭 3개 세워야 함

# 0 빈칸
# 1 벽
# 2 바이러스

# 벽을 3개 세웠을 때 안전 영역의 최대 크기

from itertools import combinations
from collections import deque
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global modlab
    Q = deque()
    vis = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if modlab[i][j] == 2:
                Q.append((i,j))
                vis[i][j] = 1
    while Q:
        curx, cury = Q.popleft()
        for dir in range(4):
            x = curx + dx[dir]
            y = cury + dy[dir]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if vis[x][y] == 1 or modlab[x][y] == 1:
                continue
            modlab[x][y] = 2
            vis[x][y] = 1
            Q.append((x,y))
    for i in range(n):
        for j in range(m):
            if modlab[i][j] == 0:
                cnt+=1
    return cnt

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

zeros = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            zeros.append([i,j])

picked_all = list(combinations(zeros, 3))

mx = 0
for picked in picked_all:
    modlab = copy.deepcopy(lab)
    for p in picked:
        i = p[0]
        j = p[1]
        modlab[i][j] = 1
    cnt = bfs()
    mx = max(mx, cnt)    

print(mx)