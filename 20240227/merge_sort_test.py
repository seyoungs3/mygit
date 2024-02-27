n = 10
arr = [15, 25, 22, 357, 16, 23, -53, 12, 46, 3]
tmp = [0] * n

# mid = (st+en)//2라고 할 때 arr[st:mid], arr[mid:en]은 이미 정렬이 되어있는 상태일 때 arr[st:mid]와 arr[mid:en]을 합친다.
def merge(st, en):
    mid = (st+en)//2
    lidx = st  # arr[st:mid]에서 값을 보기 위해 사용하는 index
    ridx = mid  # arr[mid:en]에서 값을 보기 위해 사용하는 index

    for i in range(st, en):
        if ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif arr[lidx] <= arr[ridx]:
            tmp[i] = arr[lidx]
            lidx += 1
        else:
            tmp[i] = arr[ridx]
            ridx += 1

    for i in range(st, en):
        arr[i] = tmp[i]  # tmp에 임시저장해둔 값을 arr로 다시 옮김
    

# arr[st:en]을 정렬하고 싶다.
def merge_sort(st, en):
    if en - st <= 1:  # 길이 1인 경우
        return
    mid = (st+en)//2
    merge_sort(st, mid)  # arr[st:mid]을 정렬한다.
    merge_sort(mid, en)  # arr[mid:en]을 정렬한다.
    merge(st, en)  # arr[st:mid]와 arr[mid:en]을 합친다.

merge_sort(0, n)
print(*arr)  # -53 3 12 15 16 22 23 25 46 357
