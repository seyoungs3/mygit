# 배열 합치기

# 시간초과

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted = []
while True:
    if not a and not b:
        break
    if not a:
        sorted.append(b[0])
        del b[0]
        continue
    if not b:
        sorted.append(a[0])
        del a[0]
        continue
    elif a[0] < b[0]:
        sorted.append(a[0])
        del a[0]
    elif a[0] > b[0]:
        sorted.append(b[0])
        del b[0]
    elif a[0] == b[0]:
        sorted.append(a[0])
        del a[0]
        del b[0]
    
for s in sorted:
    print(s, end=' ')