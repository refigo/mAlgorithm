// codeup C 1071~1079

//1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명)
/*
정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 개수는 알 수 없다.

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	i;

reload:
	scanf("%d", &i);
	if (i != 0)
	{
		printf("%d\n", i);
		goto reload;
	}
	return (0);
}
*/

//1072 : [기초-반복실행구조] 정수 입력받아 계속 출력하기(설명)
/*
n개의 정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

n개의 입력된 정수를 순서대로 출력해보자.

while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n, i;

	scanf("%d", &n);
reload:
	scanf("%d", &i);
	printf("%d\n", i);
	if (--n >  0) {goto reload;}
	return (0);
}
*/

//1073 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기2(설명)
/*
정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 개수는 알 수 없다.

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	i;

	while (1)
	{
		scanf("%d", &i);
		if (i == 0)
			break;
		printf("%d\n", i);
	}
	return (0);
}
*/

//1074 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	count;

	scanf("%d", &count);
	while (count > 0)
		printf("%d\n", count--);
	return (0);
}
*/

//1075 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	count;

	scanf("%d", &count);
	while (count-- > 0)
		printf("%d\n", count);
	return (0);
}
*/

//1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	char	x;
	char	current;

	scanf("%c", &x);
	current = 'a';
	do
	{
		printf("%c ", current++);
	} while (current <= x);
	return (0);
}
*/

//1077 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	i;
	int	current;

	scanf("%d", &i);
	current = 0;
	while (current <= i)
		printf("%d\n", current++);
	return (0);
}
*/

//1078 : [기초-종합] 짝수 합 구하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	i;
	int	current;
	int	sum;

	scanf("%d", &i);
	current = 0;
	sum = 0;
	while (++current <= i)
		if (current % 2 == 0)
			sum += current;
	printf("%d\n", sum);
	return (0);
}
*/

//1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기⭐️
/*
'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
*/
/*
#include <stdio.h>

int	main(void)
{
	char	x;

	do
	{
		scanf("%c ", &x);
		printf("%c\n", x);
	} while (x != 'q');
	return (0);
}
*/

