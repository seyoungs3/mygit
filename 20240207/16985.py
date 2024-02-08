# 5*5 크기의 판 5개
# 하얀 칸은 들어갈 수 있고, 검은 칸은 들어갈 수 없음
# 시계 혹은 반시계 방향으로 회전 가능
# 회전 후 판 5개를 자유로운 순서로 쌓는다

# 현재 위치한 칸에서 면으로 인접한 칸이 하얀색인 경우 그 칸으로 이동 가능
# 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출하면 우승
# 미로의 입구나 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 없으면 탈출 불가능

# 주어진 판에서 가장 적은 이동 횟수로 출구에 도달할 수 있게 했을 때 몇 번 이동을 해야하는지 구하기

# 탈출이 불가능할 경우에는 -1 출력

# 브루트 포스
# 백트래킹

# bfs함수는 잘되고있음

from collections import deque
import copy

def randrotate(): # 5개의 보드 랜덤횟수만큼 회전(적용까지 하는 함수)
    global cboards
    for num in range(1024):
        tnum = num
        k = 0
        for _ in range(5):
            mod = tnum % 4 
            tnum = tnum // 4
            for _ in range(mod):
                temp = [[0 for _ in range(5)] for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        temp[i][j] = cboards[k][4-j][i]
                cboards[k] = temp[:]
            k += 1
            
def bfs():
    global cboards
    Q = deque()
    vis = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    dist = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    if cboards[0][0][0] != 1 or cboards[4][4][4] != 1: # 입구나 출구가 1이 아닌 경우
        return -1
    elif cboards[0][0][0] == 1 and cboards[4][4][4] == 1: # 둘 다 갈 수 있는 경우에만 시작
        Q.append((0,0,0))
        vis[0][0][0] = 1
        dist[0][0][0] = 0
    while Q:
        cur = Q.popleft()
        for dir in range(6):
            x = cur[0]+dx[dir]
            y = cur[1]+dy[dir]
            z = cur[2]+dz[dir]
            if x < 0 or x >= 5 or y < 0 or y >= 5 or z < 0 or z >= 5:
                continue
            if cboards[x][y][z] != 1 or vis[x][y][z] == 1:
                continue
            Q.append((x,y,z))
            vis[x][y][z] = 1
            dist[x][y][z] = dist[cur[0]][cur[1]][cur[2]] + 1

    if dist[4][4][4] == 0:
        return -1
    return dist[4][4][4]

def placement(cur):
    global mn, cboards
    cboards = boards[:]
    if cur == 5:
        randrotate()
        temp = []
        for idx in arr:
            temp.append(cboards[idx])
        cboards = temp[:]
        move = bfs()
        # print(move)
        if move != -1: # 거리가 있는 경우에만 최솟값 갱신
            mn = min(move, mn)
        return
    for i in range(5):
        if isused[i] == 0:
            arr[cur] = i
            isused[i] = 1
            placement(cur+1)
            isused[i] = 0

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# 상하앞뒤좌우
dx = [-1,1,0,0,0,0] # 0
dy = [0,0,-1,1,0,0] # 1
dz = [0,0,0,0,-1,1] # 2

isused = [0 for _ in range(5)]
arr = [0 for _ in range(5)]
cur = 0
mn = 9999 # 가능한 가장 큰 숫자
cnt = 0
placement(0)

if mn == 9999:
    mn = -1

print(mn)
