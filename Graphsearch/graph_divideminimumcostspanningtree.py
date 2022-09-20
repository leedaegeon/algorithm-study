import sys
def find_parent(ptable, x):
    if ptable[x] != x:
        ptable[x] = find_parent(ptable, ptable[x])
    return ptable[x]
def union(ptable, x, y):
    a = find_parent(ptable, x)
    b = find_parent(ptable, y)
    if a < b:
        ptable[b] = a
    else:
        ptable[a] = b

n, m = map(int, sys.stdin.readline().strip().split())
cycle = 0
data = []
ptable = [i for i in range(n+1)]
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().strip().split())
    data.append((a, b, cost))

data.sort(key = lambda x: x[2])
total_cost = 0
biggist_cost = 0

for i in data:
    if find_parent(ptable, i[0]) != find_parent(ptable, i[1]):
        union(ptable, i[0], i[1])
        total_cost += i[2]
        biggist_cost = i[2]

print(total_cost - biggist_cost)
