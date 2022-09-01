from collections import deque
import sys


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    frontier.append((x, y))
    while frontier:
        a, b = frontier.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if field[nx][ny] == 0:
                continue
            if field[nx][ny] == 1:

                frontier.append((nx, ny))
                field[nx][ny] = field[a][b]+1
                # for i in field:
                #     print(i)
                # print("============")
n, m = map(int, sys.stdin.readline().strip().split())
field = []
frontier = deque()
cnt = 2
for i in range(n):
    ls = list(map(int, sys.stdin.readline().strip()))
    field.append(ls)

bfs(0,0)
print(field[-1][-1])