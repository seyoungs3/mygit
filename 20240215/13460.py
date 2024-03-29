# 구슬 탈출 2

# 빨간 구슬 1, 파란 구슬 1
# 빨간 구슬 빼기
# 파란 구슬이 구멍에 들어가면 안됨-> 동시에 빠져도 실패
# 중력을 이용해서 굴리기 -> 왼 오 위 아래
# 최소 몇 번 만에 빨간 구슬을 빼낼 수 있는지

# . 빈칸
# # 벽
# O 구멍
# 10번 이하로 빼낼 수 없으면 -1

# 백트래킹을 시도했으나 안됨

from itertools import product
import copy
import sys
sys.setrecursionlimit(10000000)

def turn():
    global cboard
    col = len(cboard) # 3 
    row = len(cboard[0]) # 10
    temp = [list('.' for _ in range(col)) for _ in range(row)]
    for i in range(row): # 0부터 9
        for j in range(col): # 0부터 2
            temp[i][j] = cboard[j][row-1-i]
    cboard = temp[:]

def left():
    global cboard
    col = len(cboard)
    row = len(cboard[0])
    for i in range(col):
        for j in range(row):
            if cboard[i][j] == 'R':
                idx = j
                while cboard[i][idx] != '#' and cboard[i][idx] != 'B':
                    skip = False
                    if cboard[i][idx] == 'O':
                        cboard[i][j] = '.'
                        skip = True
                        break
                    idx -= 1
                if not skip:
                    cboard[i][j] = '.'
                    cboard[i][idx+1] = 'R'
            if cboard[i][j] == 'B':
                idx = j
                while cboard[i][idx] != '#' and cboard[i][idx] != 'R':
                    skip = False
                    if cboard[i][idx] == 'O':
                        cboard[i][j] = '.'
                        skip = True
                        break
                    idx -= 1
                if not skip:
                    cboard[i][j] = '.'
                    cboard[i][idx+1] = 'B'

def up():
    global cboard
    turn()
    left()

def right():
    global cboard
    for _ in range(2):
        turn()
    left()

def down():
    global cboard
    for _ in range(3):
        turn()
    left()

def solve(cur):
    global cboard, cnt
    cnt = 0
    cboard = copy.deepcopy(board)
    if cur == 10:
        cnt = 0
        return
    for dir in func:
        dir()
        cnt += 1
        backboard = copy.deepcopy(cboard)
        if all('R' not in c for c in cboard):
            if any('B' in c for c in cboard):
                return cnt
        solve(cur+1)
        cboard = copy.deepcopy(backboard)
    return -1
      
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

func = [left, right, up, down]
ans = solve(0)
print(ans)
