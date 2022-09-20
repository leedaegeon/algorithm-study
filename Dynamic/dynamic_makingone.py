import sys
import time
sys.setrecursionlimit(500000)


# def making_one():
#     flag = 0
#     while True:
#         for i in range(4):
#             if num_dict[i] == 1:
#                 flag = 1
#                 break
#             if num_dict[i] % 5 == 0:
#                 num_dict[i] //= 5
#                 cnt[i] += 1
#             elif num_dict[i] % 3 == 0:
#                 num_dict[i] //= 3
#                 cnt[i] += 1
#             elif num_dict[i] % 2 == 0:
#                 num_dict[i] //= 2
#                 cnt[i] += 1
#             else:
#                 if flag == 0:
#                     num_dict[i] -= 1
#                     cnt[i] += 1
#
#         if flag == 1:
#             break

#
# num = int(input())
# num_dict = [0 for i in range(4)]
# cnt = [i for i in range(4)]
# for i in range(4):
#     num_dict[i] = num - i
# start = time.time()
# making_one()
#
# for i in range(4):
#     if num_dict[i] == 1:
#         print(cnt[i])
# print(time.time() - start)

# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])