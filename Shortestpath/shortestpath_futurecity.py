import sys
INF = int(1e9)

n, e = map(int, input().split())

data = [[INF]*(n+1) for i in range(n+1)]
for i in range(e):
    start, nxt = map(int, sys.stdin.readline().strip().split())

    data[start][nxt] = 1
    data[nxt][start] = 1
    data[start][start] = 0
x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            data[j][k] = min(data[j][k], data[j][i] + data[i][k])

sub1 = data[1][k]
sub2 = data[k][x]

if sub1 == INF or sub2 == INF:
    print(-1)
else:
    print(sub1 + sub2)
