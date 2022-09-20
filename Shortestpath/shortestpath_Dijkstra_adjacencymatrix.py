import sys
#메모리 초과 + 반복문을 사용한 최소비용 구하는 방식(느린방식)
INF = 987654321
#무한대 값을 int로 변환해주어야 실수형으로 계산되지 않는다.
INF = int(INF)

v, e = map(int, sys.stdin.readline().strip().split())
starting_point = int(sys.stdin.readline().strip())

data = [[0]*(v+1) for i in range(v+1)]
visited = [0 for i in range(v+1)]
min_cost = [0 for i in range(v+1)]

for i in range(e):
    u, k, w = map(int, sys.stdin.readline().strip().split())
    #인접행렬
    data[u][k] = w
#거리테이블 초기화
for i in range(1, v+1):
    min_cost[i] = INF
#시작지점 0으로 초기화
min_cost[starting_point] = 0

while True:
    #거리테이블 업데이트 확인
    print(min_cost)
    #중복된 지점을 다시 방문하면 break
    if visited[starting_point] == 0:
        visited[starting_point] = 1
        cnt = 0
        #cost updating
        for i in data[starting_point]:
            if i != 0:
                #현재 코스트와 첫번째 스타팅포인트부터 현재 스타팅포인트를 거쳐서 i번 노드로 갈때 값을 비교하여 작은 것을 선택
                min_cost[cnt] = min(min_cost[cnt], min_cost[starting_point]+i)
            cnt += 1

        min_val = INF
        #다음번 탐색할 노드
        #값이 같은 경우 낮은 번호의 노드부터 탐색 하기 위함
        for i in range(v, 0, -1):
            if min_val > min_cost[i]:
                #방문한 적 없는 노드 선택
                if visited[i] == 0:
                    min_val = min_cost[i]
                    #가장 작은 값을 갖는 인덱스 메모
                    index = i
        #min_cost배열에서 방문한적 없고, 가장 작은 path cost를 갖는 노드를 다음번 스타팅 포인트로 사용
        starting_point = index
    else:
        break

for i in min_cost[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)





