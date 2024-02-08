from itertools import permutations
from collections import deque

board = [[[[] for _ in range(5)] for _ in range(5)] for _ in range(4)]
maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

dx = [1, 0, 0, 0, 0, -1]
dy = [0, 1, -1, 0, 0, 0]
dz = [0, 0, 0, 1, -1, 0]

def solve():
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return 9999
    
    q = deque([(0, 0, 0)])
    dist[0][0][0] = 1
    
    while q:
        x, y, z = q.popleft()
        
        for dir in range(6):
            nx, ny, nz = x + dx[dir], y + dy[dir], z + dz[dir]
            
            if 0 > nx or 5 <= nx or 0 > ny or 5 <= ny or 0 > nz or 5 <= nz:
                continue
            
            if maze[nx][ny][nz] == 0 or dist[nx][ny][nz] != 0:
                continue
            
            if nx == 4 and ny == 4 and nz == 4:
                return dist[x][y][z]
            
            dist[nx][ny][nz] = dist[x][y][z] + 1
            q.append((nx, ny, nz))
    
    return 9999

def main():
    for i in range(5):
        for j in range(5):
            board[0][i][j] = list(map(int, input().split()))
    
        for j in range(5):
            board[1][i][j] = board[0][i][4 - j][:]
            
        for j in range(5):
            board[2][i][j] = board[1][i][4 - j][:]
            
        for j in range(5):
            board[3][i][j] = board[2][i][4 - j][:]
    
    order = [0, 1, 2, 3, 4]
    ans = 9999
    
    for permuted_order in permutations(order):
        for tmp in range(1024):
            brute = tmp
            
            for i in range(5):
                dir = brute % 4
                brute //= 4
                
                for j in range(5):
                    for k in range(5):
                        maze[i][j][k] = board[dir][permuted_order[i]][j][k]
            
            ans = min(ans, solve())
    
    if ans == 9999:
        ans = -1
    
    print(ans)

if __name__ == "__main__":
    main()
