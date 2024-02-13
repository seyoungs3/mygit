# 테트로미노
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노, 5종류
# n*m 종이 위에 테트로미노를 하나 놓음
# 테트로미노가 놓인 칸에 쓰여 있는 수의 합을 최대로
# 테트로미노 회전이나 대칭 가능

# brute force
# n, m = map(int, input().split())
# scores = [list(map(int, input().split())) for _ in range(n)]

tetro1 = [[1,1,1,1]]
tetro2 = [[1,1],
          [1,1]]
tetro3 = [[1,0],
          [1,0],
          [1,1]]
tetro4 = [[1,0],
          [1,1],
          [0,1]]
tetro5 = [[1,1,1],
          [0,1,0]]
tetros = [tetro1, tetro2, tetro3, tetro4, tetro5]

def rotate(arr): 
    col = len(arr) # 3
    row = len(arr[0]) # 2
    temp = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            temp[i][j] = arr[col-1-j][i]
    arr = temp[:]
    return arr

def flipx(arr): 
    col = len(arr)
    row = len(arr[0])
    temp = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(col):
        for j in range(row):
            temp[i][j] = arr[col-1-i][j]
    arr = temp[:]
    return arr
    
def flipy(arr): 
    col = len(arr)
    row = len(arr[0])
    temp = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(col):
        for j in range(row):
            temp[i][j] = arr[i][row-1-j]
    arr = temp[:]
    return arr

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

mx = 0
for tetro in tetros:
    col = len(tetro)
    row = len(tetro[0])
    for start_x in range(n-col+1):
        for start_y in range(m-row+1):
            sum = 0
            for i in range(start_x, start_x+col):
                for j in range(start_y, start_y+row):
                    if tetro[i-start_x][j-start_y] == 1:
                        sum += paper[i][j]
            mx = max(sum, mx)

print(mx)

        
