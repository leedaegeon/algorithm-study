import sys
import time
from collections import deque

start = time.time()
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())

data.sort()
query = deque()
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    query.append((a, b))

for i in range(m):
    a, b = query.popleft()
    a -= 1
    target = 1

    for x in data[a:b]:

        if target < x:
            break
        target += x
    print(target)

# print(time.time() - start)