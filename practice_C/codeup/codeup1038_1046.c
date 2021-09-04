// codeup c 1038~1046

//1038 : [기초-산술연산] 정수 2개 입력받아 합 출력하기1(설명)
/*
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
(단, 입력되는 정수는 -1073741824 ~ 1073741824 이다.)
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n1, n2;
	
	scanf("%d %d", &n1, &n2);
	printf("%lld\n", (long long)n1 + n2);
	return (0);
}
*/

//1039 : [기초-산술연산] 정수 2개 입력받아 합 출력하기2(설명)
/*
#include <stdio.h>

int	main(void)
{
	long long	n1, n2;
	
	scanf("%lld %lld", &n1, &n2);
	printf("%lld\n", n1 + n2);
	return (0);
}
*/

//1040 : [기초-산술연산] 정수 1개 입력받아 부호 바꿔 출력하기(설명)
/*
입력된 정수의 부호를 바꿔 출력해보자.
단, -2147483647 ~ +2147483647 범위의 정수가 입력된다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	num;

	scanf("%d", &num);
	printf("%d\n", -num);
	return (0);
}
*/

//1041 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	char	c;

	scanf("%c", &c);
	printf("%c\n", c + 1);
	return (0);
}
*/

//1042 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a/b);
	return (0);
}
*/

//1043 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d\n", a % b);
	return (0);
}
*/

//1044 : [기초-산술연산] 정수 1개 입력받아 1 더해 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	num;
	
	scanf("%d", &num);
	printf("%lld\n", (long long)num + 1);
	return (0);
}
*/

//1045 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기
/*
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단 0 <= a, b <= 2147483647, b는 0이 아니다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n1, n2;

	scanf("%d %d", &n1, &n2);
	printf("%lld\n", (long long)n1 + n2);
	printf("%lld\n", (long long)n1 - n2);
	printf("%lld\n", (long long)n1 * n2);
	printf("%d\n", n1 / n2);
	printf("%d\n", n1 % n2);
	printf("%.2f\n", (float)n1 / n2);
	return (0);
}
*/

//1046 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
/*
#include <stdio.h>

int	main(void)
{
	int	n1, n2, n3;
	long long	sum;

	scanf("%d %d %d", &n1, &n2, &n3);
	sum = (long long)n1 + n2 + n3;
	printf("%lld\n%.1f\n", sum, (float)sum / 3);
	return (0);
}
*/

