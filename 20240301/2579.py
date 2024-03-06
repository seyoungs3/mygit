# 계단 오르기

# 한 번에 한 계단 혹은 두 계단씩
# 연속된 세 개의 계단 불가
# 마지막 도착 계단은 반드시 밟기

# 총 점수의 최댓값

def dp(n):
    D[0][1] = S[0]
    D[0][2] = 0
    if n == 1:
        return S[0]
    D[1][1] = S[1]
    D[1][2] = S[0]+S[1]

    for i in range(2,n):
        D[i][1] = max(D[i-2][1], D[i-2][2]) + S[i]
        D[i][2] = D[i-1][1] + S[i]

    ans = max(D[n-1][1], D[n-1][2])
    return ans

n = int(input())
D = [[0,0,0] for _ in range(n)]
S = [0 for _ in range(n)]
for i in range(n):
    S[i] = int(input())
ans = dp(n)
print(ans)
