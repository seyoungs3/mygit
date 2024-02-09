# 뱀
# 사과를 먹으면 뱀 길이가 늘어남
# 벽 또는 자기자신과 부딪히면 게임 끝
# 뱀의 길이 1, 오른쪽을 향함, 맨위 맨좌측 위치

# 몸길이를 늘려 머리를 다음칸에 위치
# 벽이나 몸에 부딪히면 끝
# 이동한 칸에 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않음
# 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌

# 게임이 몇 초에 끝나는 지 계산
from collections import deque

def snake():
    global i, j, d, t
    for _ in range(l):
        x, c = input().split()
        x = int(x)
        while t < x:
            t += 1
            ni = i+dx[d]
            nj = j+dy[d]
            if ni < 0 or ni >= n or nj < 0 or nj >= n: # 벽과 부딪힌 경우
                return t
            if board[ni][nj] == 1: # 몸과 부딪힌 경우
                return t
            if board[ni][nj] != 2: # 사과를 못먹어서 몸을 줄여야 되는 경우
                tail_x, tail_y = Q.popleft() # 큐에서 삭제
                board[tail_x][tail_y] = 0 # 보드값 변경
            i = ni
            j = nj
            board[i][j] = 1 # 머리 전진
            Q.append((i, j)) # 큐에 추가
        if c == 'L': # 방향 회전
            d = (d+3) % 4
        elif c == 'D':
            d = (d+1) % 4
    while True:
        t += 1
        ni = i+dx[d]
        nj = j+dy[d]
        if ni < 0 or ni >= n or nj < 0 or nj >= n: # 벽과 부딪힌 경우
            return t
        if board[ni][nj] == 1: # 몸과 부딪힌 경우
            return t
        if board[ni][nj] != 2: # 사과를 못먹어서 몸을 줄여야 되는 경우
            tail_x, tail_y = Q.popleft() # 큐에서 삭제
            board[tail_x][tail_y] = 0 # 보드값 변경
        i = ni
        j = nj
        board[i][j] = 1 # 머리 전진
        Q.append((i, j)) # 큐에 추가  

n = int(input())
k = int(input())
board = [list(0 for _ in range(n)) for _ in range(n)]
for _ in range(k):
    ii, jj = map(int, input().split())
    board[ii-1][jj-1] = 2
dx = [0,1,0,-1]
dy = [1,0,-1,0]
board[0][0] = 1
l = int(input())
i, j, d, t = 0, 0, 0, 0
Q = deque()
Q.append((0,0))

t = snake()
print(t)
