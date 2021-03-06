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

# N, M??? ???????????? ???????????? ????????????
n, m = map(int, input().split())

# ????????? ????????? ???????????? ?????? ?????? ???????????? 0?????? ?????????
d = [[0] * m for _ in range(n)]
# ?????? ???????????? X ??????, Y ??????, ????????? ????????????
x, y, direction = map(int, input().split())
d[x][y] = 1 # ?????? ?????? ?????? ??????

# ?????? ??? ????????? ????????????
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# ???, ???, ???, ??? ?????? ??????
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# ???????????? ??????
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# ??????????????? ??????
count = 1
turn_time = 0
while True:
    # ???????????? ??????
    nx = x + dx[direction]
    ny = y + dy[direction]
    # ????????? ?????? ????????? ????????? ?????? ?????? ???????????? ?????? ??????
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # ????????? ?????? ????????? ????????? ?????? ?????? ????????? ????????? ??????
    else:
        turn_time += 1
    # ??? ?????? ?????? ??? ??? ?????? ??????
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # ?????? ??? ??? ????????? ????????????
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # ?????? ????????? ???????????? ??????
        else:
            break
        turn_time = 0

# ?????? ??????
print(count)
"""
