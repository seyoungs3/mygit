# 로봇 청소기
# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수
# 처음에 빈 칸은 전부 청소되지 않은 상태

# 1 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
# 2 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
# 바라보는 방향을 유지한 채로 후진할 수 있다면 한 칸 후진하고 1번으로
# 후진할 수 없다면 작동을 멈춤
# 3 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 반시계 방향으로 90도 회전
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않았으면 한 칸 전진
# 1번으로

# d 0북, 1동, 2남, 3서
# n m
# r c d
# 값이 0이면 청소되지 않은 빈칸, 1이면 벽
# 테두리는 무조건 벽(1)

dx = [-1,0,1,0]
dy = [0,1,0,-1]


n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

clean = 0

while True:
    if room[r][c] == 0: # 현재 칸이 청소되지 않은 경우
        room[r][c] = 2 # 현재 칸 청소
        clean += 1 # 청소한 칸 개수 업데이트
    somethingdirty = False
    for _ in range(4): # 4방향에 대해서
        d = (d+3) % 4
        if room[r+dx[d]][c+dy[d]] == 0:
            somethingdirty = True
            r += dx[d]
            c += dy[d]
            break
    if somethingdirty:
        continue
    if room[r-dx[d]][c-dy[d]] == 1:
        break
    r -= dx[d]
    c -= dy[d]

print(clean)