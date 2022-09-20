#topology sort
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())

q = [[] for i in range(n+1)]
itable = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    q[a].append(b)
    #진입차수 증가
    itable[b] += 1
index = deque()
result = []
for i in range(len(itable)):
    if itable[i] == 0:
        # 진입차수가 0이면 인덱스 테이블에 저장
        index.append(i)

while index:
    now = index.popleft()
    result.append(now)
    for i in q[now]:
        itable[i] -= 1
        if itable[i] == 0:
            index.append(i)


for i in range(1, n+1):
    print(result[i], end = " ")