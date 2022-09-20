import sys

#배열 a의 합이 최대가 되도록 b의 원소와 교환
n, k = map(int, input().strip().split())

a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

#배열 a를 오름차순으로 정렬
a.sort()
#배열 b를 내림차순으로 정렬
b.sort(reverse=True)
#최대 교체횟수 k번 만큼 반복
for i in range(k):
    #i번째 a의 원소보다 b의 원소가 더 크면 교환
    #굳이 b의 원소까지 바꿀 필요는 없다.
    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))