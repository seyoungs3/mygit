# pivot 왼쪽에는 pivot보다 작은 수
# pivot 오른쪽에는 pivot보다 큰 수
arr = [6,-8,1,12,8,3,7,-7]
pivot = arr[0]
l = 1
r = len(arr)-1

while True:
    while arr[l] < pivot:
        l += 1
    while arr[r] >= pivot:
        r -= 1
    if r < l:
        break
    # tmp = arr[l]
    # arr[l] = arr[r]
    # arr[r] = tmp
    arr[l], arr[r] = arr[r], arr[l]

# tmp = arr[r]
# arr[r] = pivot
# arr[0] = tmp
arr[0], arr[r] = arr[r], arr[0]

print(*arr)
