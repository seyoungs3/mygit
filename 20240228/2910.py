# 빈도 정렬

# 많이 등장하는 경우 앞에
# 횟수가 같으면 먼저 나온 것이 앞에

n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, key = lambda x: arr.index(x))
arr = sorted(arr, key = lambda x: arr.count(x), reverse = True)

print(*arr)
    
