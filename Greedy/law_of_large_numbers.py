# law_of_large_numbers.py

first_line = input()
second_line = input()

first_line = first_line.split(' ')
N = int(first_line[0])
M = int(first_line[1])
K = int(first_line[2])
del first_line

# exception and setting nums_array
if not (2 <= N <= 1000) or not (1 <= M <= 10000) or not (1 <= K <= 10000) or (M < K):
    print("Inputs aren't correct!")
    quit()
nums_array = list(map(int, second_line.split(' ')))
del second_line
if len(nums_array) != N:
    print("Size isn't correct!")
    quit()
for num in nums_array:
    if not (1 <= num <= 10000):
        print("The number in list isn't correct")
        quit()

# finding result
nums_array.sort(reverse=True)
result = 0
while M:
    if M >= K:
        result += nums_array[0] * K
        M -= K
    else:
        result += nums_array[0] * M
        M = 0
    if M:
        result += nums_array[1]
        M -= 1
print(result)

'''
# 3-2
## example-1

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

## example-2

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
'''
