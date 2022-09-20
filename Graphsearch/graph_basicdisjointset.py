import sys
def real_parent(ptable ,x):
    if ptable[x] != x:
        return real_parent(ptable, ptable[x])
    return x

def union(ptable, x, y):
    a = real_parent(ptable, x)
    b = real_parent(ptable, y)
    if a < b:
        ptable[b] = a
    else:
        ptable[a] = b

n, m = map(int, sys.stdin.readline().strip().split())
ptable = [i for i in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    union(ptable, x, y)


print(ptable)

for i in range(1, n+1):
    print(real_parent(ptable, i), end = " ")