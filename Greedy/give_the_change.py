# give_the_change.py

N = int(input("The chage is.. : "))
coins = [500, 100, 50, 10]
coin_num = 0

for coin in coins:
    coin_num += (N // coin)
    N = N % coin

print("The number of coins is %d" % coin_num)


'''
# Solving

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin   # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
'''
