# UDLR.py

max_size = int(input())
# input L R U D
plan = list(input().split())

position = [1, 1]

def exec_plan(c):
    if (c == 'L'):
        if position[1] == 1:
            pass
        else:
            position[1] -= 1
    elif (c == 'R'):
        if position[1] == max_size:
            pass
        else:
            position[1] += 1
    elif (c == 'U'):
        if position[0] == 1:
            pass
        else:
            position[0] -= 1
    elif (c == 'D'):
        if position[0] == max_size:
            pass
        else:
            position[0] += 1

for c in plan:
    exec_plan(c)

print(position[0], position[1])


'''
# 4-1
## example

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

" L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
'''
