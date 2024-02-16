# 연산자 끼워넣기

# 연산자 우선 순위를 무시하고 앞에서부터 진행
# 나눗셈은 정수 나눗셈

# 식의 결과가 최대인 것과 최소인 것


from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
arr =  list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

mark = ['+' for _ in range(plus)]+['-' for _ in range(minus)]+['*' for _ in range(mul)]+['/' for _ in range(div)]

mark_in_order = list(permutations(mark, n-1))

mx = -100000000000
mn = 1000000000000
a = arr.pop(0)
first_a = a

for marks in mark_in_order:
    a = first_a
    for i in range(n-1):
        if marks[i] == '+':
            a = a + arr[i]
        elif marks[i] == '-':
            a = a - arr[i]
        elif marks[i] == '*':
            a = a * arr[i]
        elif marks[i] == '/':
            if a >= 0:
                a = a // arr[i]
            elif a < 0:
                a *= -1
                a = a // arr[i]
                a *= -1
    mx = max(mx, a)
    mn = min(mn, a)

print(mx)
print(mn)