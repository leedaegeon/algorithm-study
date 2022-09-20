import sys
import heapq
INF = 987654321
INF = int(INF)

v, e = map(int, sys.stdin.readline().strip().split())
starting_point = int(sys.stdin.readline().strip())
data = [[] for i in range(v+1)]
distance = [INF] * (v + 1)

for i in range(e):
    u, k, w = map(int, sys.stdin.readline().strip().split())
    #(u에 연결된 node번호, cost)
    data[u].append((k, w))

q = []
#heap에 (거리, 노드) 형식으로 push
heapq.heappush(q, (0, starting_point))
distance[starting_point] = 0

while q:
    dist, node = heapq.heappop(q)
    #이전에 방문 한 노드라면 continue
    if distance[node] < dist:
        continue
    for i in data[node]:
        #현재 node와 연결돼 있는 i[0]번을 가는 비용이 이전에 구한 값 보다 현재 노드를 커쳐 가는 비용이 더 적은 경우 업데이트
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            #값이 정해진 노드정보를  heap에 (거리, 노드) 형식으로 push
            heapq.heappush(q, (cost, i[0]))
    print(q)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



