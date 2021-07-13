# royal_knight.py

# input position, ex) a1
position = []
for pos in input():
   position += pos

# convert char to int
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def char_to_num(position):
    ret = []
    for i in range(8):
        if col_list[i] == position[0]:
            ret.append(i + 1)
            break
    ret.append(int(position[1]))
    return ret

position_num = char_to_num(position)
col_pos = position_num[0]
row_pos = position_num[1]

# count the number of cases
count = 0

def is_valid_position(col, row):
    if 1 <= col <= 8 and 1 <= row <= 8:
        return 1
    else:
        return 0

def move_knight(count, col, row):
    count += is_valid_position(col+2, row+1)
    count += is_valid_position(col+2, row-1)
    count += is_valid_position(col-2, row+1)
    count += is_valid_position(col-2, row-1)
    count += is_valid_position(col+1, row+2)
    count += is_valid_position(col-1, row+2)
    count += is_valid_position(col+1, row-2)
    count += is_valid_position(col-1, row-2)
    return count
    
count = move_knight(count, col_pos, row_pos)
print(count)


'''
# 4-3
## example

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if nest_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''
