from collections import deque
import copy
import time

start = time.time()

v = int(input())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
time2 = [0] * (v+1)
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time2[i] = data[0]
    #-1이 맨 마지막 원소이기 때문에 그 원소 전까지 반복
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():

    result = copy.deepcopy(time2)

    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time2[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v+1):
        print(result[i])
topology_sort()

print(time.time() - start)