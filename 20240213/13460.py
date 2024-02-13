# 구슬 탈출 2

# 빨간 구슬 1, 파란 구슬 1
# 빨간 구슬 빼기
# 파란 구슬이 구멍에 들어가면 안됨-> 동시에 빠져도 실패
# 중력을 이용해서 굴리기 -> 왼 오 위 아래
# 최소 몇 번 만에 빨간 구슬을 빼낼 수 있는지

# . 빈칸
# # 벽
# O 구멍
# 10번 이하로 빼낼 수 없으면 -1

# 백트래킹 -> 기울임 함수 구현해야되는데 못해먹겠음 ㅎ
# 아니면 dfs


board = list(input())
n = len(board)
print(board)

# def backtracking(times):
#     if times == 11:
#         return -1

# n, m = map(int, input().split())
# board = [list(input()) for _ in range(n)]