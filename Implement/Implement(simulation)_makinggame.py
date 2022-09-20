import sys
n, m = map(int, sys.stdin.readline().strip().split())

x, y, direction = map(int, sys.stdin.readline().strip().split())
game_map = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))

    game_map.append(row)

print(game_map)
#북, 남
direction_type_x = [0, -1, 0, 1]
#동, 서
direction_type_y = [-1, 0, 1, 0]

rotate_cnt = 0
sea_cnt = 0
move_cnt = 1
game_map[x][y] = 1

while True:
    #1번 조건
    for i in range(4):
        #방향 탐색
        if direction == i:
            nx = x + direction_type_x[i]
            ny = y + direction_type_y[i]
    #2번 조건
    #방문한적 없고 육지면 1번조건으로
    #맵의 외곽은 바다로 둘러 쌓여 있다는 조건으로 인해 아래 if문에대한 처리는 따로 하지 않음
    if 0 <= nx < n and 0 <= ny < m:
        if game_map[nx][ny] == 0:
            #갈 수 있는 곳이면 이동
            print(nx, ny)
            print(game_map[nx][ny])
            x = nx
            y = ny
            game_map[nx][ny] = 1
            move_cnt += 1
            #움직이면 모든 카운터 초기화
            rotate_cnt = 0
            sea_cnt = 0

        elif game_map[nx][ny] == 1:
            #가고자 하는 방향이 바다인 경우
            sea_cnt += 1
            #turn left
            if direction == 0:
                direction = 3
            else:
                direction -= 1
            rotate_cnt += 1
        else:
            continue
    #4번 회전할 동안 갈 수 있는 곳이 없는 경우 또는 4면이 바다인 경우
    if rotate_cnt == 4 or sea_cnt == 4:

        for i in range(4):
            #뒤쪽으로 방향 전환
            if direction == i:
                mx = x + direction_type_x[i-1]
                my = y + direction_type_y[i-1]

        if 0 <= mx < n and 0 <= my < m:
            #뒤로 갈 수 있는 경우 이동
            if game_map[mx][my] == 0:
                print(mx, my)
                #이동했으니 카운터 초기화
                rotate_cnt = 0
                sea_cnt = 0
                x = mx
                y = my
                move_cnt += 1
                game_map[mx][my] = 1
            #아닐경우 종료
            else:
                break

print(move_cnt)