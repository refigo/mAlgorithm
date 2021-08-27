# codeup python 6063~6076

#6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)⭐️
"""
a, b = input().split()
c = (int(a) if (int(a) > int(b)) else int(b))
print(c)
"""

#6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
"""
a, b, c = map(int, input().split())
print(min(a, b, c))

d = (a if (a < b) else b) if ((a if (a < b) else b) < c) else c
print(d)
"""

#6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)
"""
a, b, c = map(int, input().split())

for i in [a, b, c]:
    if i % 2 == 0:
        print(i)
"""

#6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
"""
a, b, c = map(int, input().split())
for i in [a, b, c]:
    if i % 2 == 0:
        print("even")
    else :
        print("odd")
"""

#6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
"""
i = int(input())
if i < 0:
    if i % 2 == 0:
        print("A")
    else :
        print("B")
else :
    if i % 2 == 0:
        print("C")
    else :
        print("D")
"""

#6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
"""
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.
"""
"""
i = int(input())
if 90 <= i <= 100:
    print("A")
elif 70 <= i <= 89:
    print("B")
elif 40 <= i <= 69:
    print("C")
elif 0 <= i <= 39:
    print("D")
"""

#6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
"""
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
"""
"""
c = input()
if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else :
    print("what?")
"""

#6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
"""
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""
"""
i = int(input())
floor_i = i // 3
if floor_i == 0 or i == 12:
    print("winter")
elif floor_i == 1:
    print("spring")
elif floor_i == 2:
    print("summer")
elif floor_i == 3:
    print("fall")
"""

#6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)
"""
while True:
    i = int(input())
    if i == 0:
        break
    print(i)
"""

#6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)
"""
i = int(input())
while i:
    print(i)
    i -= 1
"""

#6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
"""
i = int(input())
while i:
    i -= 1
    print(i)
"""

#6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
"""
c = input()
m = 'a'
while m <= c:
    print(m, end=' ')
    m = chr(ord(m) + 1)
"""

#6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
"""
i = int(input())
for m in range(0, i+1):
    print(m)
"""

#6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)
"""
n = int(input())
for i in range(n + 1):
    print(i)
"""

