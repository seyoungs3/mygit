# quick sort answer

def quick_sort(st, en):
    if en <= st+1:
        return
    pivot = arr[st]
    l = st+1
    r = en-1
    while True:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] > pivot:
            r -= 1
        if l > r:
            break
        arr[l], arr[r] = arr[r], arr[l]
    arr[st], arr[r] = arr[r], arr[st]
    quick_sort(st,r)
    quick_sort(r+1,en)

arr = [15, 25, 22, 357, 16, 23, -53, 12, 46, 3]
n = 10
quick_sort(0,n)
print(*arr)