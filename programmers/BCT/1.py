# 문자열 출력하기
str = input()
print(str) 

    # another
str = input()
while True:
    if len(str) >= 1 and len(str) <= 10000000 and str != ' ':

        print(str)
        break
    else:
        continue

# a와 b 출력하기
a, b = map(int, input().strip().split(' '))
print("a = " + str(a))
print("b = " + str(b))

    # another
a, b = map(int, input().strip().split(' '))
print(f"a = {a}\nb = {b}")

# 문자열 반복해서 출력하기
a, b = input().strip().split(' ')
b = int(b)
while b != 0:
    print(a, end='')
    b -= 1

    # another
a, b = input().strip().split(' ')
b = int(b)

result = a * b
print(result)

# 대소문자 바꿔서 출력하기

# 특수문자 바꿔서 출력하기













