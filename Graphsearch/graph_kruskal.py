import sys
sys.setrecursionlimit(500000)

n, m = map(int, sys.stdin.readline().strip().split())

def findParent(ptable, x):
    if ptable[x] != x:
        ptable[x] = findParent(ptable, ptable[x])
    return ptable[x]

def union(ptable, x, y):
    a = findParent(ptable, x)
    b = findParent(ptable, y)
    if a < b:
        ptable[b] = a
    else:
        ptable[a] = b

ptable = [i for i in range(n+1)]
data = []
for i in range(m):
    x, y, cost = map(int, sys.stdin.readline().strip().split())
    data.append((x, y, cost))
#cost를 기준으로 정렬
data.sort(key = lambda x : x[2], reverse=True)
totalCost = 0
a = []
while data:
    x, y, cost = data.pop()
    #cycle 생성되면 버림
    if findParent(ptable, x) == findParent(ptable, y):
        continue
    #간선 선택 및 코스트 계산
    totalCost += cost
    union(ptable, x, y)
    #선택된 노드 추가(연결 안된 노드가 있을 때를 가정
    a.append(x)
    a.append(y)

#노드 중복 제거
b = set(a)
for i in b:
    #부모노드찾기 수행
    findParent(ptable, i)
#모든 노드가 같은 최상단 부모노드를 갖는다.
print(ptable)
print(totalCost)