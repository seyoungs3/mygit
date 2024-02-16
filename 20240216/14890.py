# 경사로

# n*n 지도
# 높이가 적혀져 있음
# 경사로를 깔 수 있음

# 경사로 조건:
# 낮은 칸에 놓으며, L개의 연속된 칸에 경사로 바닥이 모두 접해야 함
# 낮은 칸과 높은 칸의 높이 차는 1
# 낮은 칸의 높이들은 모두 같아야하고, L개의 칸이 연속

# 놓은 곳에 또 놓을 수 없음
# 높이 차가 1이 아니면 안됨
# 낮은 지점의 높이가 모두 같지 않거나, L개가 연속이 아니면 안됨
# 놓다가 범위를 벗어나면 안됨

n, L = map(int(input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

ans = 2*n

for i in range(n):
    for j in range(n):
        if board[i][j] != board[i][j+1]:
            if board[i][j] - board[i][j+1] == -1:
                for k in range(L):
                    if j-k < 0:
                        ans -= 1
                        break
                    if board[i][j] != board[i][j-k]:
                        ans -= 1
                        break
            elif board[i][j] - board[i][j+1] == 1:
                for k in range(L):
                    if j+k >= n:
                        ans -= 1
                        break
                    if board[i][j] != board[i][j+k]:
                        ans -= 1
                        break


