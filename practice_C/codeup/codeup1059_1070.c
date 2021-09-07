// codeup c 1059~1070

//1059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)
/*
정수 1개가 입력된다.
-2147483648 ~ +2147483647

비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	i;

	scanf("%d", &i);
	printf("%d\n", ~i);
	return (0);
}
*/
/*
#include <stdio.h>
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0')

int	main(void)
{
	int	i;

	scanf("%d", &i);
	printf("%d:\t", i);
	printf(BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(i));
	printf("%d:\t", ~i);
	printf(BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(~i));
	return (0);
}
*/

//1060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a & b);
	return (0);
}
*/
/*
#include <stdio.h>
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0')

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("  "BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(a));
	printf("\n& ");
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(b));
	printf("\n----------");
	printf("\n  ");
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(a & b));
	printf("\n");
	return (0);
}
*/

//1061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a | b);
	return (0);
}
*/
/*
#include <stdio.h>
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0')

int	main(void)
{
	int	a, b;
	int	c;

	scanf("%d %d", &a, &b);
	printf("  "BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(a));
	printf("\n| ");
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(b));
	printf("\n----------");
	printf("\n  ");
	c = (a | b);
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(c));
	printf("\n");
	return (0);
}
*/

//1062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a^b);
	return (0);
}
*/
/*
#include <stdio.h>
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0')

int	main(void)
{
	int	a, b;
	int	c;

	scanf("%d %d", &a, &b);
	printf("  "BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(a));
	printf("\n| ");
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(b));
	printf("\n----------");
	printf("\n  ");
	c = (a ^ b);
	printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(c));
	printf("\n");
	return (0);
}
*/

//1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a > b) ? a : b);
	return (0);
}
*/

//1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b, c;
	int	min;

	scanf("%d %d %d", &a, &b, &c);
	min = (((a<b)?a:b) < c) ? ((a<b)?a:b) : c;
	printf("%d\n", min);
	return (0);
}
*/

//1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
/*
#include <stdio.h>

int	print_even(int num)
{
	if (num % 2 == 0)
	{
		printf("%d\n", num);
		return (1);
	}
	return (0);
}

int	main(void)
{
	int	num[3];
	int	i;

	scanf("%d %d %d", &num[0], &num[1], &num[2]);
	i = 0;
	while (3 - (i))
		print_even(num[i++]);
	return (0);
}
*/

//1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)
/*
#include <stdio.h>

void	print_even_or_odd(int num)
{
	if (num % 2 == 0)
		printf("even\n");
	else
		printf("odd\n");
}

int	main(void)
{
	int	num[3];
	int	i;

	scanf("%d %d %d", &num[0], &num[1], &num[2]);
	i = 0;
	while (3 - (i))
		print_even_or_odd(num[i++]);
	return (0);
}
*/

//1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기(설명)
/*
#include <stdio.h>

void	print_sign(int num)
{
	if (num < 0)
		printf("minus\n");
	else
		printf("plus\n");
}

void	print_even_or_odd(int num)
{
	if (num % 2 == 0)
		printf("even\n");
	else
		printf("odd\n");
}

int	main(void)
{
	int	num;

	scanf("%d", &num);
	print_sign(num);
	print_even_or_odd(num);
	return (0);
}
*/

//1068 : [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기(설명)
/*
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
*/
/*
#include <stdio.h>

void	print_evaluation(int score)
{
	if (90 <= score)
		printf("A");
	else if (70 <= score)
		printf("B");
	else if (40 <= score)
		printf("C");
	else if (0 <= score)
		printf("D");
	printf("\n");
}

int	main(void)
{
	int	score;

	scanf("%d", &score);
	print_evaluation(score);
	return (0);
}
*/

//1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(설명)
/*
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
*/
/*
#include <stdio.h>

void	print_content(char eval)
{
	switch (eval)
	{
		case 'A':
			printf("best!!!");
			break;
		case 'B':
			printf("good!!");
			break;
		case 'C':
			printf("run!");
			break;
		case 'D':
			printf("slowly~");
			break;
		default:
			printf("what?");
	}
	printf("\n");
}

int	main(void)
{
	char	eval;

	scanf("%c", &eval);
	print_content(eval);
	return (0);
}
*/

//1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)
/*
월이 입력될 때 계절 이름이 출력되도록 해보자.

예
월 : 계절 이름
 12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
*/
/*
#include <stdio.h>

void	print_season(int month)
{
	switch (month)
	{
		case 12:
		case 1:
		case 2:
			printf("winter");
			break;
		case 3:
		case 4:
		case 5:
			printf("spring");
			break;
		case 6:
		case 7:
		case 8:
			printf("summer");
			break;
		case 9:
		case 10:
		case 11:
			printf("fall");
			break;
	}
	printf("\n");
}

int	main(void)
{
	int	month;

	scanf("%d", &month);
	print_season(month);
	return (0);
}
*/

