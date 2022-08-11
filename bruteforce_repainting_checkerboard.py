# -*- coding: utf-8 -*-

import sys

n, m = map(int, sys.stdin.readline().strip().split())
chess = []
for i in range(n):
    chess.append(list(sys.stdin.readline().strip()))
black_first = 0
white_first = 0

result = []
for i in range(n-7):
    for j in range(m-7):

        for l in range(i, i+8):
            for k in range(j, j+8):
               if (l + k) % 2 == 0:
                   if chess[l][k] != "W":
                       white_first += 1
                   if chess[l][k] != "B":
                       black_first += 1
               else:
                   if chess[l][k] != "B":
                       white_first += 1
                   if chess[l][k] != "W":
                       black_first += 1

        result.append(black_first)
        result.append(white_first)
        black_first = 0
        white_first = 0

print(min(result))