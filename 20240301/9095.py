# 1, 2, 3 더하기

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0 for _ in range(12)]
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(11):
        if i <= 3:
            continue
        arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    print(arr[n])