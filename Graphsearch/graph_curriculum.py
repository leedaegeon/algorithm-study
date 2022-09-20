import sys
from collections import deque
import time
start = time.time()

n = int(input())
time2, a = map(int, sys.stdin.readline().strip().split())
inpt_lst = deque()

inpt_lst.append((time2, 0, -1))
for i in range(1, n):
    inpt_lst.append(tuple(map(int, sys.stdin.readline().strip().split())))

time_ls = []
num = 1
while inpt_lst:
    data = inpt_lst.popleft()

    maxi = 0
    # print(num)
    # print(data)
    for i in data[1:]:

        if i != -1 and i != 0:
            # print(time_ls[i-1] + data[0], i)
            # print(time_ls)
            if maxi < time_ls[i-1] + data[0]:
                maxi = time_ls[i-1] + data[0]

    # print("===========")
    if maxi != 0:
        time_ls.append(maxi)
    else:
        time_ls.append(data[0])
    num += 1

for i in range(n):
    print(time_ls[i])
print(time.time() - start)