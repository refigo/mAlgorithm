// codeup C 1047~1058

//1047 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	num;

	scanf("%d", &num);
	printf("%d\n", num << 1);
	return (0);
}
*/

//1048 : [기초-비트시프트연산] 한 번에 2의 거듭제곱 배로 출력하기(설명)
/*
정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10
*/
/*
#include <stdio.h>

int	main(void)
{
	int	a;
	int	b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a << b);
	return (0);
}
*/

//1049 : [기초-비교연산] 두 정수 입력받아 비교하기1(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a;
	int	b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a > b));
	return (0);
}
*/

//1050 : [기초-비교연산] 두 정수 입력받아 비교하기2(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a;
	int	b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a == b));
	return (0);
}
*/

//1051 : [기초-비교연산] 두 정수 입력받아 비교하기3(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a <= b));
	return (0);
}
*/

//1052 : [기초-비교연산] 두 정수 입력받아 비교하기4(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a != b));
	return (0);
}
*/

//1053 : [기초-논리연산] 참 거짓 바꾸기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	i;

	scanf("%d", &i);
	printf("%d\n", !i);
	return (0);
}
*/

//1054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a && b));
	return (0);
}
*/

//1055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (a || b));
	return (0);
}
*/

//1056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)⭐️
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	//printf("%d\n", (a && !b));	//wrong
	printf("%d\n", ((a && !b) || (!a && b)));
	return (0);
}
*/

//1057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", ((a && b) || (!a && !b)));
	return (0);
}
*/

//1058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", (!a && !b));
	return (0);
}
*/

