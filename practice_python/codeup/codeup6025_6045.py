# codeup python 6025~6045

#6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기(설명)(py)
"""
a, b = input().split()
print(int(a) + int(b))
"""

#6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기(설명)(py)
"""
a = input()
b = input()
print(float(a) + float(b))
"""

#6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1(설명)(py)⭐️
"""
a = int(input())
print('%x'% a)
"""

#6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2(설명)(py)⭐️
"""
a = int(input())
print('%X'% a)
"""

#6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)(py)⭐️
"""
#a = input()
n = int(input(), 16)
print('%o' % n)
"""

#6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기(설명)(py)⭐️
"""
c = ord(input())
print(c)
"""

#6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기(설명)(py)⭐️
"""
c = int(input())
print(chr(c))
"""

#6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기(설명)(py)
"""
i = int(input()) * (-1)
print(i)
"""

#6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)
"""
c = ord(input())
print(chr(c + 1))
"""

#6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
"""
a, b = input().split()
print(int(a) - int(b))
"""

#6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
"""
a, b = input().split()
print(float(a) * float(b))
"""

#6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py)
"""
s, n = input().split()
n = int(n)
print(s * n)
"""

#6037 : [기초-산술연산] 문장 여러 번 출력하기(설명)(py)
"""
n = int(input())
s = input()
print(s * n)
"""

#6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)⭐️
"""
n, p = input().split()
n = int(n)
p = int(p)
result = 1
for _ in range(p):
    result *= n
print(result)
"""
"""
n, p = input().split()
print(int(n) ** int(t))
"""

#6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
"""
n, p = input().split()
print(float(n) ** float(p))
"""

#6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)
"""
a, b = input().split()
print(int(a) // int(b))
"""

#6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
"""
a, b = input().split()
print(int(a) % int(b))
"""

#6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)⭐️
"""
f = float(input())
print(format(f, ".2f"))
"""

#6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
"""
f1, f2 = input().split()
print(format(float(f1)/float(f2), ".3f"))
"""

#6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
"""
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))
"""

#6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)
"""
a, b, c = input().split()
sum = int(a) + int(b) + int(c)
print(sum, format(sum / 3, ".2f"))
"""

