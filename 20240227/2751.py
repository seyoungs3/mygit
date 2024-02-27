import sys

input = sys.stdin.readline

def merge(st, en):
    global tmp
    mid = (st+en) // 2
    lidx = st
    ridx = mid
    for i in range(st, en):
        if lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif arr[lidx] <= arr[ridx]:
            tmp[i] = arr[lidx]
            lidx += 1
        elif arr[lidx] > arr[ridx]:
            tmp[i] = arr[ridx]
            ridx += 1

    for i in range(st, en):
        arr[i] = tmp[i]



def merge_sort(st, en):
    if en - st == 1:
        return
    mid = (st + en) // 2
    merge_sort(st,mid)
    merge_sort(mid,en)
    merge(st,en)


n = int(input())
arr = []
tmp = [0]*n
for i in range(n):
    arr.append(int(input()))
merge_sort(0,n)
for a in arr:
    print(a)