# 역원소 정렬

# 원소를 거꾸로 뒤집고 그 원소를 오름차순으로 정렬

arr = []
while True:
    line = list(map(int, input().split()))
    arr += line
    if len(arr) == arr[0]+1:
        break
    
del arr[0]
narr = []
for num in arr:
    num = list(str(num))
    tmp = ''
    for i in range(len(num)):
        tmp += num[-1-i]
    tmp = int(tmp)
    narr.append(tmp)

narr.sort()

for num in narr:
    print(num)