# n = int(input())
#
# fear = list(map(int, input().split()))
# sub = [0 for i in range(max(fear)+1)]
# fear.sort()
#
# for i in fear:
#     sub[i] += 1
# gcnt = 0
# add = 0
#
# print(sub)
# for i in range(1, max(fear)+1):
#     #이전에 그룹에 들어가지 못한 모험가를 캐리오버(이전값에서 보태줌)
#     sub[i] += add
#     #필요인원수보다 적합한 인원수가 더 크다면
#     if sub[i] >= i:
#         #최소인원으로 그룹을 만든다
#         gcnt += sub[i] // i
#     #이전 그룹에 들어가지 못했다면 캐리오버로 저장
#     add = (sub[i] % i)
#     print(sub)
#
# print(gcnt)

#답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    print(i)
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력