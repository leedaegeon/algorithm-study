# -*- coding: utf-8 -*-

n = int(input())
tw = 0
th = 0
w = []
h = []
ls = []
for i in range(n):
    tw, th = map(int, input().split())
    w.append(tw)
    h.append(th)

for i in range(n):
    rank = 0
    for j in range(n):
        if w[i] < w[j] and h[i] < h[j]:
            rank += 1
    ls.append(rank+1)

for i in range(n):
    print(ls[i], end=" ")

