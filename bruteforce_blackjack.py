# -*- coding: utf-8 -*-

n, m = map(int, input().split())  # n은 카드의 개수, M은 총합
max = 0
card = list(map(int, input().split()))
result = 0
# 3개 뽑기
for i in range(0, n - 2):

    for j in range(i + 1, n - 1):

        for k in range(j + 1, n):
            max = card[i] + card[j] + card[k]

            if max <= m and max > result:
                result = max
print(result)