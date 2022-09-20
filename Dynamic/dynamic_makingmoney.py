
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
sol = [10001 for i in range(m)]
sol[0] = 0
#m은 목표로 하는 화폐 크기
for i in range(1, m):
    #a는 화폐 종류
    for j in a:
        if i >= j:
            sol[i] = min(sol[i], sol[i-j] + 1)
    print(sol)

if sol[m-1] != 10001:
    print(sol[m-1])
else:
    print(-1)
