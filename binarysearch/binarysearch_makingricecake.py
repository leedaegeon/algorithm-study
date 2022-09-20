import sys

def bin_search(cake, target, start, end):

    while start <= end:
        total_size = 0
        mid = (start + end) // 2

        for i in cake:
            #떡 크기보다 더 큰 크기로 자르면 음의 값이 나오므로 걸러줘야한다.
            if i-mid > 0:
                total_size += (i - mid)
        if total_size < target:
            end = mid - 1
        elif total_size > target:
            start = mid + 1
        elif total_size == target:
            return mid

    return mid
n, m = map(int, sys.stdin.readline().rstrip().split())

cake = list(map(int, sys.stdin.readline().rstrip().split()))

print(bin_search(cake, m, 0, max(cake)-1))


# 4 6
# 19 15 10 17