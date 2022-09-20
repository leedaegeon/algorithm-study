import sys
def findParent(ptable, x):
    if ptable[x] != x:
        ptable[x] = findParent(ptable, ptable[x])
    return ptable[x]

def union(a, b):
    x = findParent(ptable, a)
    y = findParent(ptable, b)
    if x<y:
        ptable[y] = x
    else:
        ptable[x] = y

n, m = map(int, sys.stdin.readline().strip().split())
ptable = [i for i in range(n+1)]

for i in range(m):
    inst, a, b = map(int, sys.stdin.readline().strip().split())
    if inst == int(0):
        union(a, b)
    else:
        if findParent(ptable, a) == findParent(ptable, b):
            print("Yes")
        else:
            print("No")