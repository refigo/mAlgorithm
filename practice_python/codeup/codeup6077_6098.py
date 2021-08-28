# codeup python 6077~6098

#6077 : [기초-종합] 짝수 합 구하기(설명)(py)
"""
n = int(input())
s = 0
for i in range(n + 1):
    if i % 2 == 0:
        s += i
print(s)
"""

#6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)
"""
while True:
    char = input()
    print(char)
    if char == 'q':
        break
"""

#6079 : [기초-종합] 언제까지 더해야 할까?(py)
"""
max_s = int(input())
s = 0
for i in range(1, max_s + 1):
    s += i
    if s >= max_s:
        print(i)
        break
"""

#6080 : [기초-종합] 주사위 2개 던지기(설명)(py)
"""
a, b = map(int, input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)
"""

#6081 : [기초-종합] 16진수 구구단 출력하기(py)⭐️
"""
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)
"""
"""
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, "*%X"%i, "=%X"%(n*i), sep='')
"""

#6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
"""
n = int(input())
for i in range(1, n+1):
    remainder = i % 10
    if remainder == 3 or remainder == 6 or remainder == 9:
        print('X', end=' ')
    else :
        print(i, end=' ')
"""

#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
"""
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1
print(count)
print(r*g*b)
"""

#6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
"""
1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.
"""
"""
h, b, c, s = map(int, input().split())
size = h * b * c * s / 8 / 1024 / 1024
print(format(size, ".1f"), "MB")
"""

#6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
"""
이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.
"""
"""
w, h, b = map(int, input().split())
size = w * h * b / 8 / 1024 / 1024
print(format(size, ".2f"), "MB")
"""

#6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
"""
언제까지 합을 계산할 지, 정수 1개를 입력받는다.
단, 입력되는 자연수는 100,000,000이하이다.

1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
그때까지의 합을 출력한다.
"""
"""
n = int(input())
s = 0
for i in range(1, n+1):
    s += i
    if s >= n:
        print(s)
        break
"""

#6087 : [기초-종합] 3의 배수는 통과(설명)(py)
"""
n = int(input())
for i in range(1, n+1):
    if i % 3 != 0:
        print(i, end=' ')
"""

#6088 : [기초-종합] 수 나열하기1(py)
"""
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 100)

n번째 수를 출력한다.
"""
"""
a, d, n = map(int, input().split())
print(a + d*(n-1))

for _ in range(1, n):
    a += d
print(a)
"""

#6089 : [기초-종합] 수 나열하기2(py)
"""
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 10)

n번째 수를 출력한다.
"""
"""
a, r, n = map(int, input().split())
for _ in range(n - 1):
    a *= r
print(a)
"""

#6090 : [기초-종합] 수 나열하기3(py)
"""
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

n번째 수를 출력한다.

예를 들어
1 -1 3 -5 11 -21 43 ... 은
1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.
"""
"""
a, m, d, n = map(int, input().split())
for _ in range(n - 1):
    a = a * m + d
print(a)
"""

#6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
"""
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.
"""
"""
a, b, c = map(int, input().split())
n = 1
while not (n % a == 0 and n % b == 0 and n % c == 0):
    n += 1
print(n)
"""

#6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
"""
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
"""
"""
n = int(input())
a = list(map(int, input().split()))

d = []
for _ in range(24):
    d.append(0)

for i in a:
    d[i] += 1

for count in d[1:]:
    print(count, end=' ')
"""

#6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
"""
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
"""
"""
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(a[n - (i+1)], end=' ')

print()
for i in range(n-1, -1, -1):
    print(a[i], end=' ')
"""

#6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
"""
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단,
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.
"""
"""
n = int(input())
a = list(map(int, input().split()))
print(min(a))

m = a[0]
for i in range(n):
    if a[i] < m:
        m = a[i]
print(m)
"""

#6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)⭐️
"""
바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 똑같은 좌표는 입력되지 않는다.

흰 돌이 올려진 바둑판의 상황을 출력한다.
흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.
"""
"""
n = int(input())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]

base = []
for i in range(0, 20):
    base.append([])
    for j in range(0, 20):
        base[i].append(0)

for i in range(n):
    a[i], b[i] = map(int, input().split())
    base[a[i]][b[i]] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(base[i][j], end=' ')
    print()
"""

#6096 : [기초-리스트] 바둑알 십자 뒤집기(py)⭐️
"""
십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
"""
"""
base = []
for i in range(19):
    base.append(list(map(int, input().split())))

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if base[x-1][j] == 0:
            base[x-1][j] = 1
        else :
            base[x-1][j] = 0
    for i in range(19):
        if base[i][y-1] == 0:
            base[i][y-1] = 1
        else :
            base[i][y-1] = 0

for i in range(19):
    for j in range(19):
        print(base[i][j], end=' ')
    print()
"""

#6097 : [기초-리스트] 설탕과자 뽑기(py)
"""
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
"""
"""
h, w = map(int, input().split())
base = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0:
        for i in range(l):
            base[x][y+i] = 1
    elif d == 1 :
        for i in range(l):
            base[x+i][y] = 1

for i in range(h):
    for j in range(w):
        print(base[i][j], end=' ')
    print()
"""

#6098 : [기초-리스트] 성실한 개미(py)
"""
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

성실한 개미가 이동한 경로를 9로 표시해 출력한다.
"""
"""
base = []
for _ in range(10):
    base.append(list(map(int, input().split())))

x, y = 1, 1
while True:
    if base[x][y] == 2:
        base[x][y] = 9
        break
    base[x][y] = 9
    if base[x][y+1] == 0 or base[x][y+1] == 2:
        y += 1
    elif base[x+1][y] == 0 or base[x+1][y] == 2:
        x += 1
    else :
        break

for i in range(10):
    for j in range(10):
        print(base[i][j], end=' ')
    print()
"""

#make two-dimensional list(array)
"""
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
        print(d[i][j], end=' ')
    print()

print()

d_2 = [[0 for _ in range(20)] for _ in range(20)]
for i in range(20):
    for j in range(20):
        print(d_2[i][j], end=' ')
    print()
"""

