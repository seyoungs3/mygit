# 단어 정렬

# 길이가 짧은 것부터
# 길이가 같으면 사전순으로
# 중복된 단어는 제거

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr.sort()

arr = sorted(arr, key = lambda x : len(x))

for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        print(arr[i])
