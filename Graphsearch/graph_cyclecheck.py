import sys

def real_parent(ptable ,x):
    if ptable[x] != x:
        return real_parent(ptable, ptable[x])
    return x

def improved_real_parent(ptable ,x):
    if ptable[x] != x:
        ptable[x] = real_parent(ptable, ptable[x])
    return ptable[x]

def union(ptable, x, y):
    global cycle
    a = improved_real_parent(ptable, x)
    b = improved_real_parent(ptable, y)
    if a < b:
        ptable[b] = a
    elif a > b:
        ptable[a] = b
    #싸이클체크 읽기 쉽게 만든 코드
    else:
        cycle = True

n, m = map(int, sys.stdin.readline().strip().split())
ptable = [i for i in range(n+1)]
cycle = False
for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    #함수 호출 전에 싸이클 체크하는 방법
    # if improved_real_parent(ptable, x) == improved_real_parent(ptable, y):
    #     cycle = True
    #     break
    # else:

    union(ptable, x, y)
    if cycle:
        break
if cycle:
    print("there is a cycle")
else:
    print("there is no cycle")

