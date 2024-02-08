def randrotate(): # 5개의 보드 랜덤횟수만큼 회전(적용까지)
    for num in range(1024):
        temp = num
        arr = []
        for _ in range(5):
            mod = temp % 4
            arr.append(mod)
            temp //= 4
    idx = 0
    for board in boards:
        for _ in range(arr[idx]):
            rotate(board)
        idx += 1