// codeup c 1028~1030

//1028 : [기초-데이터형] 정수 1개 입력받아 그대로 출력하기1(설명)⭐️
/*
정수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 정수의 범위는 0 ~ 4,294,967,295 이다.)
*/
/*
#include <stdio.h>

int	main(void)
{
	unsigned int	num;

	scanf("%u", &num);
	printf("%u\n", num);
	return (0);
}
*/

//1029 : [기초-데이터형] 실수 1개 입력받아 그대로 출력하기2(설명)⭐️
/*
실수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 실수의 범위는 +- 1.7*10^-308 ~ +- 1.7*10^308 이다.)

소수점 아래 숫자가 11개 이하인 실수 1개가 입력된다.
(단, 입력되는 실수의 범위는 +- 1.7*10-308 ~ +- 1.7*10308 이다.)

입력된 실수를 소수점 이하 11자리까지 반올림하여 출력한다.
*/
/*
#include <stdio.h>

int	main(void)
{
	double	d_num;

	scanf("%lf", &d_num);
	printf("%.11lf", d_num);
	return (0);
}
*/

//1030 : [기초-데이터형] 정수 1개 입력받아 그대로 출력하기3(설명)
/*
정수 1개를 입력받아 그대로 출력해보자.
단, 입력되는 정수의 범위는
-9,223,372,036,854,775,808 ~ +9,223,372,036,854,775,807 이다.
*/
/*
#include <stdio.h>

int	main(void)
{
	long long int	num;

	scanf("%lld", &num);
	printf("%lld\n", num);
	return (0);
}
*/

