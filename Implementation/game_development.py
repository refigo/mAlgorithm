# game_development.py

#input data
N, M = map(int, input().split())
status = list(map(int, input().split()))
game_map = []
visit_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
    tmp = [0, 0, 0, 0]
    visit_map.append(tmp)    # initialize visit_map

position = [status[0], status[1]]
direction = status[2]
if game_map[position[0]][position[1]] != 0:
    print("drowned")
    quit()
directs = [0, 1, 2, 3]
visit_map[position[0]][position[1]] = 1
count = 1

def is_valid_position(y, x):
    if (game_map[y][x] == 0) and (visit_map[y][x] == 0):
        return 1
    else: return 0

def is_valid_moving(choosing_direction):
    next_y = position[0]
    next_x = position[1]
    if (0 == choosing_direction):
        next_y -= 1
    elif (1 == choosing_direction):
        next_x += 1
    elif (2 == choosing_direction):
        next_y += 1
    elif (3 == choosing_direction):
        next_x -= 1
    if (is_valid_position(next_y, next_x)):
        return 1
    else: return 0

def move_back(direction):
    if (0 == choosing_direction):
        position[0] += 1
    elif (1 == choosing_direction):
        position[1] -= 1
    elif (2 == choosing_direction):
        position[0] -= 1
    elif (3 == choosing_direction):
        position[1] += 1
    if game_map[position[0]][position[1]] == 0:
        return 1
    else: return 0

def move_position(choosing_direction):
    global count
    if (0 == choosing_direction):
        position[0] -= 1
    elif (1 == choosing_direction):
        position[1] += 1
    elif (2 == choosing_direction):
        position[0] += 1
    elif (3 == choosing_direction):
        position[1] -= 1
    visit_map[position[0]][position[1]] = 1
    print("moving position")
    count += 1

while (True):
    choosing_direction = direction
    while (True):
        choosing_direction = directs[choosing_direction - 1]
        if (is_valid_moving(choosing_direction)):
            move_position(choosing_direction)
            print(position)
            direction = choosing_direction
            break
        if (choosing_direction == direction):
            if not move_back(direction):
                print(count)
                quit()


"""
# 4-4
## example

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시물레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
"""
