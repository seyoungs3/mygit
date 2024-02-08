N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

chkCnt = 0  # 방향 탐지 횟수

while True:
    # 청소하지 않은 빈 칸일 경우 청소
    if board[x][y] == 0:
        ans += 1
        board[x][y] = -1  # 청소된 칸이라고 표시
    cleaned = False  # 네 방향 중 청소가 된 곳이 있는지

    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽으로 회전
        if board[x + dx[d]][y + dy[d]] == 0: # 청소해야 되는 칸이면
            x += dx[d] # 이동
            y += dy[d]
            cleaned = True
            break

    if cleaned:
        continue

    # 뒤가 벽으로 막혀 있으면, 로봇 청소기 종료
    if board[x - dx[d]][y - dy[d]] == 1:
        break

    # 막혀 있지 않을 경우, 후진
    x -= dx[d]
    y -= dy[d]

print(ans)
