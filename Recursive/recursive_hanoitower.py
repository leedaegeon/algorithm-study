# This is a sample Python script.
# -*- coding: utf-8 -*-
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
sys.setrecursionlimit(500000)

def recursive_hanoi(n, a, b, c):
    if n == 1:
        #남은 1개를 a에서 c로
        print(a, c)
    else:
        #1번에서 3번으로 옮긴다
        recursive_hanoi(n-1, a, c, b)
        print(a, c)
        #2번에서 3번으로
        recursive_hanoi(n-1, b, a, c)



n = int(input())
cnt = pow(2, n)-1
print(cnt)
recursive_hanoi(n, 1, 2, 3)