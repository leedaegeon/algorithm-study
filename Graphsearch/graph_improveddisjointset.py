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
    a = improved_real_parent(ptable, x)
    b = improved_real_parent(ptable, y)
    if a < b:
        ptable[b] = a
    else:
        ptable[a] = b

n, m = map(int, sys.stdin.readline().strip().split())
ptable = [i for i in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    union(ptable, x, y)


#각 원소별로 경로 압축을 수행하면 부모테이블이 모두 최 상단 부모를 가리키게 된다.
for i in range(1, n+1):
    print(improved_real_parent(ptable, i), end = " ")

print()
print(ptable)
