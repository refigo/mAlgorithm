// test_scanf.c

#include <stdio.h>

int	main(void)
{
	int	i_num[9] = {};
	char	c_num[9] = {};
	int	k;
	
	for (k = 0; k < 9; k++)
		scanf("%d", &i_num[k]);
	for (k = 0; k < 9; k++)
		scanf("%c", &c_num[k]);
	printf("\n=== test scanf %%d ===\n");
	for (k = 0; k < 9; k++)
		printf("i_num[%d] == %c\n", k, i_num[k]);
	printf("\n=== test scanf %%c ===\n");
	for (k = 0; k < 9; k++)
		printf("c_num[%d] == %c\n", k, c_num[k]);
	return (0);
}



