# count_times_with_3.py

N = int(input())

def find_three_in_set():
    find = 0
    for num in range(60):
        num_set = list(map(int, str(num)))
        for each in num_set:
            if each == 3:
                find += 1
                break
    return find

count_three_in_set = find_three_in_set()

count_in_hour = (2 * 60 * count_three_in_set) - (count_three_in_set * count_three_in_set)

if N < 3:
    total = (N + 1) * count_in_hour
elif N < 13:
    total = (N * count_in_hour) + (60 * 60)
elif N < 23:
    total = ((N - 1) * count_in_hour) + (2 * (60 * 60))

print(total)


'''
# 4-2
## example
(Brute Forcing)

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
'''
