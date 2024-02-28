# 1로 만들기

n = int(input())
D = [0] * (n+1)

D[1] = 0
for i in range(2,n+1):
    a, b, c = 10**6+1, 10**6+1, 10**6+1
    if i % 3 == 0:
        a = D[i//3] + 1
    if i % 2 == 0:
        b = D[i//2] + 1
    c = D[i-1]+1
    D[i] = min(a,b,c)
    if i == n:
        break

print(D[n])