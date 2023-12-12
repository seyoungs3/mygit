import sys
input = sys.stdin.readline

n = int(input())

A = [0]*n

for i in range(n):
    A[i] = int(input())

stack = []
number = 1

for i in range(n):
    