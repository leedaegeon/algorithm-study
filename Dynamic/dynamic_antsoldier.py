import sys

n = int(input())
x = list(map(int, input().split()))

for i in range(2, n):
    x[i] = max(x[i-1], x[i-2] + x[i])

print(x)