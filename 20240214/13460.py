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

# 백트래킹

from itertools import permutations

def turn():
    global board
    col = len(board) # 3 
    row = len(board[0]) # 10
    temp = [list('.' for _ in range(col)) for _ in range(row)]
    for i in range(row): # 0부터 9
        for j in range(col): # 0부터 2
            temp[i][j] = board[j][row-1-i]
    board = temp[:]

def left():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                idx = j
                while board[i][idx] != '#' and board[i][idx] != 'B':
                    skip = False
                    if board[i][idx] == 'O':
                        board[i][j] = '.'
                        skip = True
                        break
                    idx -= 1
                if not skip:
                    board[i][j] = '.'
                    board[i][idx+1] = 'R'
            if board[i][j] == 'B':
                idx = j
                while board[i][idx] != '#' and board[i][idx] != 'R':
                    skip = False
                    if board[i][idx] == 'O':
                        board[i][j] = '.'
                        skip = True
                        break
                    idx -= 1
                if not skip:
                    board[i][j] = '.'
                    board[i][idx+1] = 'B'

def up():
    turn()
    left()

def right():
    for _ in range(2):
        turn()
    left()

def down():
    for _ in range(3):
        turn()
    left()


func = [left(), up(), right(), down()]
def solve():
    arr = permutations(func, 1)
    


n,m = map(int, input().split())
board = [list(input()) for _ in range(n)]

