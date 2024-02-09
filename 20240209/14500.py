# 테트로미노
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노, 5종류
# n*m 종이 위에 테트로미노를 하나 놓음
# 테트로미노가 놓인 칸에 쓰여 있는 수의 합을 최대로
# 테트로미노 회전이나 대칭 가능

# brute force
# n, m = map(int, input().split())
# scores = [list(map(int, input().split())) for _ in range(n)]

tetro1 = [1,1,1,1]
tetro2 = [[1,1],
          [1,1]]
tetro3 = [[1,0],
          [1,0],
          [1,0],
          [1,1]]
tetro4 = [[1,0],
          [1,1],
          [0,1]]
tetro5 = [[1,1,1],
          [0,1,0]]
tetros = [tetro1, tetro2, tetro3, tetro4, tetro5]

def rotate(arr): # 정상 동작 확인 완료
    col = len(arr) # 3
    row = len(arr[0]) # 2
    temp = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            temp[i][j] = arr[col-1-j][i]
    arr = temp[:]
    return arr

# def flipx():
    
# def flipy():

tetro3 = rotate(tetro3)
for line in tetro3:
    print(line)