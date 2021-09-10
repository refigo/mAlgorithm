// codeup C 1092~1099

//1092 : [기초-종합] 함께 문제 푸는 날(설명)
/*
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	a, b, c;
	int	result;

	scanf("%d %d %d", &a, &b, &c);
	result = 0;
	while (++result)
		if ((result % a) == 0 && \
			(result % b) == 0 && \
			(result % c) == 0)
			break;
	printf("%d\n", result);
	return (0);
}
*/

//1093 : [기초-1차원배열] 이상한 출석 번호 부르기1(설명)⭐️
/*
출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n;
	int	called_counter[23];
	int	called_number;

	for (int i = 0; i < 23; i++)
		called_counter[i] = 0;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &called_number);
		called_counter[called_number - 1] += 1;
	}
	for (int i = 0; i < 23; i++)
		printf("%d ", called_counter[i]);
	return (0);
}
*/

//1094 : [기초-1차원배열] 이상한 출석 번호 부르기2(설명)⭐️
/*
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n;
	int	number_array[10000] = {};

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", number_array + i); 
	for (int i = 1; i <= n; i++)
		printf("%d ", number_array[n - i]);
	return (0);
}
*/

//1095 : [기초-1차원배열] 이상한 출석 번호 부르기3(설명)
/*
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	n;
	int	number_array[10000] = {};
	int	min;
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", number_array + i);
	min = number_array[0];
	for (int i = 1; i < n; i++)
		if (number_array[i] < min)
			min = number_array[i];
	printf("%d\n", min);
	return (0);
}
*/

//1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
/*
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.

흰 돌이 올려진 바둑판의 상황을 출력한다.
흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	base[19][19];
	int	n;
	int	x, y;

	for (int i = 0; i < 19; i++)
		for (int j = 0; j < 19; j++)
			base[i][j] = 0;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %d", &x, &y);
		base[x - 1][y - 1] = 1;
	}
	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
			printf("%d ", base[i][j]);
		printf("\n");
	}

	return (0);
}
*/

//1097 : [기초-2차원배열] 바둑알 십자 뒤집기(설명)
/*
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

십자 뒤집기 결과를 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	base[19][19];
	int	i, j;
	int	n;
	int	x, y;

	for (i = 0; i < 19; i++)
		for (j = 0; j < 19; j++)
			scanf("%d", &base[i][j]);
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %d", &x, &y);
		for (j = 0; j < 19; j++)
		{
			if (base[x - 1][j] == 0)
				base[x - 1][j] = 1;
			else
				base[x - 1][j] = 0;
		}
		for (i = 0; i < 19; i++)
		{
			if (base[i][y - 1] == 0)
				base[i][y - 1] = 1;
			else
				base[i][y - 1] = 0;
		}
	}
	for (i = 0; i < 19; i++)
	{
		for (j = 0; j < 19; j++)
			printf("%d ", base[i][j]);
		printf("\n");
	}
	return (0);
}
*/

//1098 : [기초-2차원배열] 설탕과자 뽑기
/*
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

입력값의 정의역은 다음과 같다.

1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.
*/

//Using a double pointer
/*
#include <stdio.h>
#include <stdlib.h>

int	**malloc_2d_array(int h, int w)
{
	int	**ret;
	int	i, j;

	ret = (int **)malloc(sizeof(int *) * h);
	if (!ret)
		return (0);
	for (i = 0; i < h; i++)
	{
		ret[i] = (int *)malloc(sizeof(int) * w);
		if (!ret[i])
			return (0);
	}
	for (i = 0; i < h; i++)
		for (j = 0; j < w; j++)
			ret[i][j] = 0;
	return (ret);
}

void	free_2d_array(int **base, int h)
{
	for (int i = 0; i < h; i++)
		free(base[i]);
	free(base);
}

void	set_base(int **base, int h, int w)
{
	int	n;
	int	l, d, x, y;

	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %d %d %d", &l, &d, &x, &y);
		if (d == 0)
		{
			while (l--)
			{
				base[x-1][y-1] = 1;
				y++;
			}
		}
		else if (d == 1)
		{
			while (l--)
			{
				base[x-1][y-1] = 1;
				x++;
			}
		}
	}
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
			printf("%d ", base[i][j]);
		printf("\n");
	}
}

int	main(void)
{
	int	h, w;
	int	**base;

	scanf("%d %d", &h, &w);
	base = malloc_2d_array(h, w);
	if (!base)
		return (-1);
	set_base(base, h, w);
	free_2d_array(base, h);
	return (0);
}
*/

//1099 : [기초-2차원배열] 성실한 개미
/*
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.


10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

성실한 개미가 이동한 경로를 9로 표시해 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	int	base[10][10];
	int	x, y;

	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
			scanf("%d", &base[i][j]);
	x = 1;
	y = 1;
	while (1)
	{
		if (base[x][y] == 2)
		{
			base[x][y] = 9;
			break;
		}
		base[x][y] = 9;
		if (base[x][y+1] == 0 || base[x][y+1] == 2)
			y++;
		else if (base[x+1][y] == 0 || base[x+1][y] == 2)
			x++;
		else
			break;
	}
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			printf("%d ", base[i][j]);
		}
		printf("\n");
	}
	return (0);
}
*/


// how to allocate a 2D array
/*
//Using a single pointer
#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	h, w;
	int	n;
	int	l, d, x, y;
	int	**base;

	scanf("%d %d", &h, &w);
	base = (int *)malloc(sizeof(int) * (h * w));
	if (!base)
		return (-1);
	for (int i = 0; i < (h * w); i++)
	{
		base[i] = 0;
		printf("%d ", base[i]);
		if ((i + 1) % w == 0)
			printf("\n");
	}
	return (0);
}
*/

//Using a double pointer
/*
#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	h, w;
	int	n;
	int	l, d, x, y;
	int	**base;
	int	i, j;

	scanf("%d %d", &h, &w);
	base = (int **)malloc(sizeof(int *) * h);
	if (!base)
		return (-1);
	for (i = 0; i < h; i++)
	{
		base[i] = (int *)malloc(sizeof(int) * w);
		if (!base[i])
			return (-1);
	}
	for (i = 0; i < h; i++)
	{
		for (j = 0; j < w; j++)
		{
			base[i][j] = 0;
			printf("%d ", base[i][j]);
		}
		printf("\n");
	}
	return (0);
}
*/

