from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def num_ice(x, y):
    global n
    global m
    global cnt
    #while문을 돌리기위한 append
    frontier.append((x, y))
    field[x][y] = 1
    while frontier:
        #2번 이상의 반복일 때 의미를 갖는 x, y
        x, y = frontier.popleft()

        for i in range(4):
            #상하좌우 살피기
            nx = x + dx[i]
            ny = y + dy[i]
            #값 초과라면 다시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #해당 필드가 0이면 1로 바꾼 뒤 재진행
            if field[nx][ny] == 0:
                field[nx][ny] = 1
                frontier.append((nx, ny))

    #덩어리 개수 계산이니 이 함수가 호출된 횟수만 세면 됨
    cnt += 1

# def dfs(x, y):
#     global m
#     global n
#     global cnt
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return
#     if field[x][y] == 0:
#         field[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)



cnt = 0
n, m = map(int, sys.stdin.readline().strip().split())
field = []
frontier = deque()

for i in range(n):
    ls = list(map(int, sys.stdin.readline().strip()))
    field.append(ls)

#맵에서 시작할 수 있는 지점이 있다면 함수호출
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            num_ice(i, j)
            print(i, j)
            # dfs(i, j)
            # cnt += 1
print(field)
print(cnt)