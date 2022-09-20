import sys

# def bin_search_looply(stock, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == stock[mid]:
#             return mid
#         elif target < stock[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
def count_sort(stock, cnt):
    for i in stock:
        cnt[i-1] += 1



n = int(sys.stdin.readline().rstrip())
stock = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = [0 for i in range(max(stock))]
m = int(sys.stdin.readline().rstrip())
stuff = list(map(int, sys.stdin.readline().rstrip().split()))

stock.sort()
sol = []
# for i in stuff:
    # sol.append(bin_search_looply(stock, i, 0, n-1))

# for i in sol:
#     if i == None:
#         print("No")
#     else:
#         print("Yes")

count_sort(stock, cnt)

for i in stuff:
    if cnt[i-1] != 0:
        print("Yes", end = " ")
    else:
        print("No", end = " ")

