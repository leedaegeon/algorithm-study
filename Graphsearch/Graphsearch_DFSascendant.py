import sys
from collections import deque

sys.setrecursionlimit(50000000)
def dfs():
    global cnt
    global enqueue
    global visited
    global initree
    while enqueue:
        node = enqueue.popleft()
        for i in sorted(initree[node - 1]):
            if visited[i] == 0:
                visited[i] = cnt
                cnt += 1
                enqueue.append(i)
                dfs()

v, e, r = map(int,sys.stdin.readline().split())
initree = [[] for i in range(v)]
visited = [0 for i in range(v+1)]

for i in range(e):
    u, v2 = map(int, sys.stdin.readline().split())
    initree[u - 1].append(v2)
    initree[v2 - 1].append(u)

enqueue = deque()
enqueue.append(r)
visited[r] = 1
cnt = 2

dfs()

print('\n'.join(map(str, visited[1:])))

