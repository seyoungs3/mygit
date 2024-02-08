# 5*5 크기의 판 5개
# 1은 들어갈 수 있고, 0은 들어갈 수 없음
# 시계 혹은 반시계 방향으로 회전 가능
# 회전 후 판 5개를 자유로운 순서로 쌓는다

# 현재 위치한 칸에서 면으로 인접한 칸이 하얀색인 경우 그 칸으로 이동 가능
# 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출하면 우승
# 미로의 입구나 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 없으면 탈출 불가능

# 주어진 판에서 가장 적은 이동 횟수로 출구에 도달할 수 있게 했을 때 몇 번 이동을 해야하는지 구하기

# 탈출이 불가능할 경우에는 -1 출력

# 브루트 포스
# 백트래킹

# 예제 5 빼고 통과함

from collections import deque
from itertools import permutations

def func(): # 5개의 보드 랜덤횟수만큼 회전(적용까지 하는 함수)
    global mn, boards
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
                        temp[i][j] = boards[k][4-j][i]
                boards[k] = temp[:]
            k += 1
        arr = permutations(idx,5)
        arr = list(arr)
        for i in arr:
            temp = []
            for index in i:
                temp.append(boards[index])
            boards = temp[:]
            move = bfs()
            mn = min(move, mn)
            if mn == 12:
                return 12
            
def bfs():
    global boards
    Q = deque()
    dist = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    if boards[0][0][0] != 1 or boards[4][4][4] != 1: # 입구나 출구가 1이 아닌 경우
        return 9999
    elif boards[0][0][0] == 1 and boards[4][4][4] == 1: # 둘 다 갈 수 있는 경우에만 시작
        Q.append((0,0,0))
    while Q:
        cur = Q.popleft()
        for dir in range(6):
            x = cur[0]+dx[dir]
            y = cur[1]+dy[dir]
            z = cur[2]+dz[dir]
            if x < 0 or x >= 5 or y < 0 or y >= 5 or z < 0 or z >= 5:
                continue
            if boards[x][y][z] != 1 or dist[x][y][z] != 0:
                continue
            Q.append((x,y,z))
            dist[x][y][z] = dist[cur[0]][cur[1]][cur[2]] + 1
            if x == 4 and y == 4 and z == 4:
                return dist[x][y][z]
    return 9999


boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# 상하앞뒤좌우
dx = [-1,1,0,0,0,0] # 0
dy = [0,0,-1,1,0,0] # 1
dz = [0,0,0,0,-1,1] # 2

idx = [0,1,2,3,4]
cur = 0
mn = 9999 # 가능한 가장 큰 숫자
cnt = 0
func()

if mn == 9999:
    mn = -1

print(mn)
