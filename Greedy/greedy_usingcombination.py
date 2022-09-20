import itertools
import sys
#볼링공 고르기 문제

#볼링공 개수 최대무게
n, m = map(int, sys.stdin.readline().strip().split())
#볼링공 번호별 무게
ls = sys.stdin.readline().strip().split()
#mC2
a = list(itertools.combinations(ls, 2))

cnt = 0
for i in a:
    #무게가 같은 원소 카운트
    if i[0] == i[1]:
        cnt += 1
#조합 - 무게가 같은 공을 고른경우
print(len(a)-cnt)