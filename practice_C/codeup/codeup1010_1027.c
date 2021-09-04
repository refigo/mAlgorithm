// codeup c 1010~1027

//1010 : [기초-입출력] 정수 1개 입력받아 그대로 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	num;

	scanf("%d", &num);
	printf("%d", num);
	return (0);
}
*/

//1011 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	char	c;

	scanf("%c", &c);
	printf("%c", c);
	return (0);
}
*/

//1012 : [기초-입출력] 실수 1개 입력받아 그대로 출력하기(설명)⭐️
/*
#include <stdio.h>

int	main(void)
{
	float	f;

	scanf("%f", &f);
	printf("%f", f);
	return (0);
}
*/

//1013 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	a, b;

	scanf("%d %d", &a, &b);
	printf("%d %d", a, b);
	return (0);
}
*/

//1014 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	char	c_1, c_2;

	scanf("%c %c", &c_1, &c_2);
	printf("%c %c", c_2, c_1);
	return (0);
}
*/

//1015 : [기초-입출력] 실수 입력받아 둘째 자리까지 출력하기(설명)⭐️
/*
#include <stdio.h>

int	main(void)
{
	float	x;

	scanf("%f", &x);
	printf("%.2f", x);
	return (0);
}
*/

//1017 : [기초-입출력] 정수 1개 입력받아 3번 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	x;

	scanf("%d", &x);
	printf("%d %d %d", x, x, x);
	return (0);
}
*/

//1018 : [기초-입출력] 시간 입력받아 그대로 출력하기(설명)⭐️
/*
#include <stdio.h>

int	main(void)
{
	char	*s;

	scanf("%s", s);
	printf("%s", s);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	int	h, m;

	scanf("%d:%d", &h, &m);
	printf("%d:%d", h, m);
	return (0);
}
*/

//1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기⭐️
/*
#include <stdio.h>

int	main(void)
{
	int	y, m, d;

	scanf("%d.%d.%d", &y, &m, &d);
	printf("%04d.%02d.%02d", y, m, d);
	return (0);
}
*/

//1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기⭐️
/*
#include <stdio.h>

int	main(void)
{
	int	n1, n2;

	scanf("%d-%d", &n1, &n2);
	printf("%06d%07d", n1, n2);
	return (0);
}
*/

//1021 : [기초-입출력] 단어 1개 입력받아 그대로 출력하기(설명)⭐️
/*
//Output : (null)
#include <stdio.h>

int	main(void)
{
	char	*s;

	scanf("%s", s);
	printf("%s", s);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	char	data[51] = "";

	scanf("%s", data);
	printf("%s", data);
	return (0);
}
*/

//1022 : [기초-입출력] 문장 1개 입력받아 그대로 출력하기(설명)⭐️⭐️
/*
//Runtime Error:Segmentation fault
#include <stdio.h>

int	main(void)
{
	char	*s;
	
	fgets(s, 2000, stdin);
	printf("%s", s);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	char	data[2001];

	fgets(data, 2000, stdin);
	printf("%s", data);
	return (0);
}
*/

//1023 : [기초-입출력] 실수 1개 입력받아 부분별로 출력하기(설명)⭐️
/*
실수 1개가 입력된다.
(단, 입력값은 절댓값이 10000을 넘지 않으며, 소수점 이하 자릿수는 최대 6자리까지이고
0이 아닌 숫자로 시작한다.)
*/
/*
Input:
1.414213

Output:
1
41421296(Wrong)

#include <stdio.h>

int	main(void)
{
	float	x;
	
	scanf("%f", &x);
	printf("%d\n", (int)x);
	x -= (int)x;
	while ((x - (int)x) != 0.0)
	{
		x *= 10.0;
	}
	printf("%d", (int)x);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	int	x, y;

	scanf("%d.%d", &x, &y);
	printf("%d\n%d", x, y);
	return (0);
}
*/

//1024 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	char	data[21];
	
	scanf("%s", data);
	for (int i = 0; data[i] != '\0'; i++)
	{
		printf("\'%c\'\n", data[i]);
	}
	return (0);
}
*/

//1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)⭐️
/*
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

다섯 자리로 이루어진 1개의 정수를 입력받는다.
(단, 10,000 <= 입력받는 수 <= 99,999 )

각 자리의 숫자를 분리해 한 줄에 하나씩 [ ]속에 넣어 출력한다.
*/
/*
//extention ver
#include <stdio.h>

int	num_exp(int num, int count)
{
	int	init_num = num;

	while (--count > 0)
		num *= init_num;
	return (num);
}

int	main(void)
{
	int	num;
	int	test_num;
	int	count;

	scanf("%d", &num);
	test_num = num;
	count = -1;
	while (test_num)
	{
		test_num /= 10;
		count++;
	}
	while (count)
	{
		printf("[%d", (num / num_exp(10, count)));
		for (int i = 0; i < count; i++)
		{
			printf("0");
		}
		printf("]\n");
		num %= ((num / num_exp(10, count)) * num_exp(10, count));
		count--;
	}
	printf("[%d]\n", num);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	char	data[6];

	scanf("%s", data);
	for (int i = 0; data[i] != '\0'; i++)
	{
		printf("[%c", data[i]);
		for (int j = 4; j - i > 0; j--)
			printf("0");
		printf("]\n");
	}
	return (0);
}
*/

//1026 : [기초-입출력] 시분초 입력받아 분만 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	h, m, s;

	scanf("%d:%d:%d", &h, &m, &s);
	printf("%d\n", m);
	return (0);
}
*/

//1027 : [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기(설명)
/*
#include <stdio.h>

int	main(void)
{
	int	y, m, d;
	
	scanf("%04d.%02d.%02d", &y, &m, &d);
	printf("%02d-%02d-%04d", d, m, y);
	return (0);
}
*/

