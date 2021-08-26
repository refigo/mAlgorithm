# codeup python 6046~6062

#6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)⭐️
"""
i = int(input())
print(2 * i)
print(i << 1)
"""

#6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)
"""
a, b = input().split()
print(int(a) << int(b))
"""

#6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)
"""
a, b = input().split()
print(int(a) < int(b))
"""

#6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)
"""
a, b = input().split()
print(int(a) == int(b))
"""

#6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)
"""
a, b = input().split()
print(int(a) <= int(b))
"""

#6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)
"""
a, b = input().split()
print(int(a) != int(b))
"""

#6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)⭐️
"""
i = int(input())
print(i != 0)
print(bool(i))
"""

#6053 : [기초-논리연산] 참 거짓 바꾸기(설명)(py)
"""
i = int(input())
print(not bool(i))
"""

#6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)
"""
a, b = input().split()
print(bool(int(a)) and bool(int(b)))
"""

#6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
"""
a, b = input().split()
print(bool(int(a)) or bool(int(b)))
"""

#6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)⭐️
"""
a, b = input().split()
print(bool(int(a)) != bool(int(b)))

c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))
"""

#6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)⭐️
"""
a, b = input().split()
print(bool(int(a)) == bool(int(b)))

c = bool(int(a))
d = bool(int(b))
print(((not c) and (not d)) or (c and d))
"""

#6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)⭐️
"""
a, b = input().split()
print((not bool(int(a))) and (not bool(int(b)))) 
print(not (bool(int(a)) or bool(int(b))))
"""

#6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)⭐️
"""
i = int(input())
print(~i)
"""

#6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)
"""
a, b = input().split()
print(int(a) & int(b))
"""

#6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
"""
a, b = input().split()
print(int(a) | int(b))
"""

#6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
"""
a, b = input().split()
print(int(a) ^ int(b))
"""

