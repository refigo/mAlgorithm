# number_card_game.py

N, M = map(int, input().split())
matrix = []
for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

# finding number card
select_num = min(matrix[0])
select_row = 0
for i in range(1, N):
    if select_num < min(matrix[i]):
        select_num = min(matrix[i])
        select_row = i
print(min(matrix[select_row]))


'''
# 3-3
## example-1
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수' 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

## example-2
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
'''
