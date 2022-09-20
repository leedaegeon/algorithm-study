import sys

def bin_search_recursion(array, target, start, end):
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        bin_search_recursion(array, target, start, mid-1)
    elif target > array[mid]:
        bin_search_recursion(array, target, mid+1, end)



n, target = map(int, input().split())

array = list(map(int, input().split()))

x = bin_search_recursion(array, target, 0, n-1)
if x == None:
    print("원소가 존재하지 않는다")
else:
    print(array[x])

