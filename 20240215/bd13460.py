# cheated
# 바킹독 해답

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
board = [input() for _ in range(n)]

red, blue = (0, 0), (0, 0)

# Find the initial positions of red and blue balls
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            blue = (i, j)
            board[i] = board[i][:j] + '.' + board[i][j + 1:] # 'B'를 '.'으로 변경
        elif board[i][j] == 'R':
            red = (i, j)
            board[i] = board[i][:j] + '.' + board[i][j + 1:] # 'R'을 '.'으로 변경
            

# Initialize distance array
dist = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque([(red[0], red[1], blue[0], blue[1])])
    dist[red[0]][red[1]][blue[0]][blue[1]] = True

    while queue:
        rx, ry, bx, by = queue.popleft()
        cnt = dist[rx][ry][bx][by]

        if cnt >= 10:
            return -1

        for i in range(4):
            n_rx, n_ry, n_bx, n_by = rx, ry, bx, by

            while board[n_bx + dx[i]][n_by + dy[i]] == '.':
                n_bx += dx[i]
                n_by += dy[i]

            if board[n_bx + dx[i]][n_by + dy[i]] == 'O':
                continue

            while board[n_rx + dx[i]][n_ry + dy[i]] == '.':
                n_rx += dx[i]
                n_ry += dy[i]

            if board[n_rx + dx[i]][n_ry + dy[i]] == 'O':
                return cnt + 1

            if (n_rx, n_ry) == (n_bx, n_by):
                if i == 0:
                    n_ry = n_ry - 1 if ry < by else n_by - 1
                elif i == 1:
                    n_rx = n_rx - 1 if rx < bx else n_bx - 1
                elif i == 2:
                    n_ry = n_ry + 1 if ry > by else n_by + 1
                else:
                    n_rx = n_rx + 1 if rx > bx else n_bx + 1

            if dist[n_rx][n_ry][n_bx][n_by]:
                continue

            dist[n_rx][n_ry][n_bx][n_by] = cnt + 1
            queue.append((n_rx, n_ry, n_bx, n_by))

    return -1

# Initialize the distance array
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                dist[i][j][k][l] = False

result = bfs()
print(result)
