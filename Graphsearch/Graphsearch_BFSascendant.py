import sys
from collections import deque
v, e, r = map(int,sys.stdin.readline().split())
initree = [[] for i in range(v)]
visited = [0 for i in range(v+1)]
enqueue = deque()
enqueue.append(r)
visited[r] = 1
cnt = 2

for i in range(e):
    u, v2 = map(int, sys.stdin.readline().split())
    initree[u-1].append(v2)
    initree[v2-1].append(u)
while enqueue:
    node = enqueue.popleft()
    for i in sorted(initree[node-1]):
        if visited[i] == 0:
            visited[i] = cnt
            cnt +=1
            enqueue.append(i)

print('\n'.join(map(str, visited[1:])))


