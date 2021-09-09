// codeup C 1080~1091

//1080 : [기초-종합] 언제까지 더해야 할까?
/*
1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	input;
	int	sum;
	int	i;

	scanf("%d", &input);
	sum = 0;
	i = 0;
	while (sum < input)
		sum += ++i;
	printf("%d\n", i);
	return (0);
}
*/

//1081 : [기초-종합] 주사위를 2개 던지면?(설명)
/*
1부터 n까지, 1부터 m까지 숫자가 적힌
서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n, m;

	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			printf("%d %d\n", i, j);
	return (0);
}
*/

//1082 : [기초-종합] 16진수 구구단?
/*
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	x;

	scanf("%X", &x);
	for (int i = 1; i < 16; i++)
		printf("%X*%X=%X\n", x, i, (x*i));
	return (0);
}
*/

//1083 : [기초-종합] 3 6 9 게임의 왕이 되자!(설명)
/*
10 보다 작은 정수 1개가 입력된다.
(1 ~ 9)

1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9인 경우 그 수 대신 영문 대문자 X 를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	x;

	scanf("%d", &x);
	for (int i = 1; i <= x; i++)
	{
		if (i % 3 == 0)
			printf("X ");
		else
			printf("%d ", i);
	}
	return (0);
}
*/

//1084 : [기초-종합] 빛 섞어 색 만들기(설명)
/*
빨녹파(r, g, b) 각 빛의 강약에 따른 가짓수(0 ~ 128))가 공백을 사이에 두고 입력된다.
예를 들어, 3 3 3 은 각 색깔 빛에 대해서 그 강약에 따라 0~2까지 3가지의 색이 있음을 의미한다.

만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	r, g, b;

	scanf("%d %d %d", &r, &g, &b);
	for (int i = 0; i < r; i++)
		for (int j = 0; j < g; j++)
			for (int k = 0; k < b; k++)
				printf("%d %d %d\n", i, j, k);
	printf("%d\n", r*g*b);
	return (0);
}
*/

//1085 : [기초-종합] 소리 파일 저장용량 계산하기(설명)⭐️
/*
h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.

필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 둘째 자리에서 반올림해 첫째 자리까지 출력하고 MB를 공백을 두고 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	j, b, c, s;

	scanf("%d %d %d %d", &j, &b, &c, &s);
	printf("%.1f MB\n", ((float)j*b*c*s/8/1024/1024));
	return (0);
}
*/

//1086 : [기초-종합] 그림 파일 저장용량 계산하기(설명)
/*
w, h, b 가 공백을 두고 입력된다.
단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.

필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력한 뒤 MB를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	w, h, b;

	scanf("%d %d %d", &w, &h, &b);
	printf("%.2lf MB\n", (double)w*h*b/8/1024/1024);
	return (0);
}
*/

//1087 : [기초-종합] 여기까지! 이제 그만~(설명)
/*
언제까지 합을 계산할 지, 정수 1개를 입력받는다.
단, 입력되는 자연수는 100,000,000이하이다.

1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
그때까지의 합을 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	x;
	int	sum;

	scanf("%d", &x);
	sum = 0;
	for (int i = 1; sum < x; i++)
		sum += i;
	printf("%d\n", sum);
	return (0);
}
*/

//1088 : [기초-종합] 3의 배수는 통과?(설명)
/*
정수 1개를 입력받는다.
(1 ~ 100)

1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
3의 배수는 출력하지 않는다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	x;

	scanf("%d", &x);
	for (int i = 1; i <= x; i++)
		if (i % 3 != 0)
			printf("%d ", i);
	return (0);
}
*/

//1089 : [기초-종합] 수 나열하기1
/*
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 100)

n번째 수를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	a, d, n;

	scanf("%d %d %d", &a, &d, &n);
	while (--n)
		a += d;
	printf("%d\n", a);
	return (0);
}
*/

//1090 : [기초-종합] 수 나열하기2⭐️
/*
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 10)

n번째 수를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	long long	a;
	int	r, n;

	scanf("%lld %d %d", &a, &r, &n);
	while (--n)
		a *= r;
	printf("%lld\n", a);
	return (0);
}
*/

//1091 : [기초-종합] 수 나열하기3
/*
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째 수를 출력하는 프로그램을 만들어보자.

시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

n번째 수를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	long long	a;
	int	m, d, n;

	scanf("%lld %d %d %d", &a, &m, &d, &n);
	while (--n)
		a = a * m + d;
	printf("%lld\n", a);
	return (0);
}
*/

