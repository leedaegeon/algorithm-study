import sys
import heapq
INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().strip().split())
#node 개수만큼 선언
data = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    # node, cost
    data[x].append((y, z))
q = []
# q <- cost, starting point
heapq.heappush(q, (0, c))
distance[c] = 0

while q:

    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in data[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# print(distance)
cnt = 0
maxi = 0

for i in range(1, n+1):
    if i != c and distance[i] != INF:
        cnt += 1
        if distance[i] > maxi:
            maxi = distance[i]
print(cnt, maxi)