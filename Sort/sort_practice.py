from collections import deque
import sys
import math
def selection_sort(array):
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        pivot = i
        for j in range(i+1, len(array)):
            if array[pivot] > array[j]:
                #가장 작은 데이터 선택
                pivot = j
        #임의로 선택한 데이터와 가장 작은 데이터를 스왑
        print(pivot)
        array[pivot], array[i] = array[i], array[pivot]
    print(array)

#0이 먼저 앞쪽을 오면서 정렬
#앞부터 정렬이 완료됨
def insertion_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                print(i, j)
                print(array)
                array[j-1], array[j] = array[j], array[j-1]
    print(array)

#9가 먼저 뒤쪽으로 가면서 정렬
#뒤부터 정렬이 완료됨
def bubble_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                print(i, j)
                print(array)
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

def quicksort(a):
    pivot = 0
    low = []
    high = []
    same = []
    b = []
    #피봇 구하기
    if len(a) <= 1:
        return a
    mid = math.trunc(len(a) / 2)
    #pivot을 설정하는 단계
    #최대한 중간값으로 설정
    if a[0] > a[-1]:
        if a[0] < a[mid]:
            pivot = a[0]
        else:
            pivot = a[mid]
    else:
        if a[-1] < a[mid]:
            pivot = a[-1]
        else:
            pivot = a[mid]

    #pivot보다 작으면 low리스트 크면 high 리스트 같으면 same 리스트에 넣는다.
    for i in a:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            same.append(i)
    #크기별로 분할 후 각 리스트에 퀵정렬을 재귀적으로 적
    return quicksort(low) + quicksort(same) + quicksort(high)

def count_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    #빈도를 저장하기위한 리스트
    count_ls = [0 for i in range(len(array))]
    #빈도 저장
    for i in array:
        count_ls[i] += 1
    #각 인덱스를 인덱스별 빈도만큼 출력
    for i in range(len(array)):
        for j in range(count_ls[i]):
            print(i, end = " ")

# selection_sort()
# insertion_sort()
# print("==============")
# bubble_sort()
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# print(quicksort(array))

count_sort()
