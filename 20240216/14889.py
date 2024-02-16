# 스타트와 링크

# S(ij)는 i번 사람과 j번 사람이 같은 팀일 때 팀에 더해지는 능력치
# 팀 능력치 = 팀에 속한 모든 쌍의 능력치의 합
# S(ij)와 S(ji)는 다를 수도 있음
# S(ij) + S(ji)

# 스타트 팀과 링크 팀의 능력치 차이를 최소로

# cheated

# 시간 초과

from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

team = [0] * n
team[n//2:] = [1] * (n//2)
ans = float('inf')

for perm in permutations(team):
    diff = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] != perm[j]:
                continue
            elif perm[i] == 0:
                diff += (a[i][j]+a[j][i])
            elif perm[i] == 1:
                diff -= (a[i][j]+a[j][i])
    ans = min(ans, abs(diff))

print(ans)