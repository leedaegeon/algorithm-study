import sys
import heapq
#메모리초과 코드
INF = 987654321
#무한대 값을 int로 변환해주어야 실수형으로 계산되지 않는다.
INF = int(INF)

v, e = map(int, sys.stdin.readline().strip().split())
starting_point = int(sys.stdin.readline().strip())

data = [[0]*(v+1) for i in range(v+1)]
min_cost = [INF]*(v+1)

for i in range(e):
    u, k, w = map(int, sys.stdin.readline().strip().split())
    #u 에서 k까지의 비용 w
    #인덱싱을 통해 cost를 저장하면 연결되어있지 않은 노드까지 0으로 초기화 해야해서 메모리를 불필요하게 사용
    data[u][k] = w

q = []
#코스트, 노드번호
heapq.heappush(q, (0, starting_point))
min_cost[starting_point] = 0

while q:
    dist, node = heapq.heappop(q)
    #최소 비용 결정 이후에 해당 노드를 다시 계산하는 경우 continue
    if min_cost[node] < dist:
        continue

    #cost update
        #i가 j번 노드랑 연결 안되어 있으면 continue
    for j in range(len(data[node])):
        if data[node][j] == 0:
            continue
        #cost = 현재 노드까지 오는데 드는 비용 + j까지 가는 비용
        cost = dist + data[node][j]

        if cost < min_cost[j]:
            min_cost[j] = cost
            heapq.heappush(q, (min_cost[j], j))
    print(q)
# print(min_cost)



for i in min_cost[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)





