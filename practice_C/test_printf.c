// test_printf.c

/*
#include <stdio.h>

int	main(void)
{
	printf("%5.0d\n", 1);
	printf("%5.d", 123); printf("%5.0d", 123); printf("%5.-2d", 123); printf(%5.*d, -2, 9);
	printf("%5.d", 0); printf("%5.0d", 0); printf("%5.-2d", 0); printf(%5.*d, -2, 0);
	return (0);
}
*/

// printf d, i
/*
#include <stdio.h>

int	main(void)
{
	printf("=== test %%d ===\n");
	printf("%d\n", -99);
	printf("%d\n", -0143);
	printf("%d\n", -0x63);
	printf("%d\n", -0x63);
	
	printf("\n");
	printf("=== test %%i ===\n");
	printf("%i\n", -99);
	printf("%i\n", -0143);
	printf("%i\n", -0x63);
	printf("%i\n", -0x63);
	return (0);
}
*/


// scanf d, i
/*
#include <stdio.h>

int	main(void)
{
	int	num;

	printf("=== test %%d ===\n");
	printf("Decimal : ");
	scanf("%d", &num);
	printf("%d\n", num);
	printf("Octal : ");
	scanf("%d", &num);
	printf("%d\n", num);
	printf("Hexadecimal : ");
	scanf("%d\n", &num);
	printf("%d\n", num);

	while (getchar() != '\n');
	printf("\n");

	printf("=== test %%i ===\n");
	printf("Decimal : ");
	scanf("%i", &num);
	printf("%i\n", num);
	printf("Octal : ");
	scanf("%i", &num);
	printf("%i\n", num);
	printf("Hexadecimal : ");
	scanf("%i", &num);
	printf("%i\n", num);
	return (0);
}
*/
/*
#include <stdio.h>

int	main(void)
{
	printf("\nCase:\n%%03.d, 99\nOutput:\n");
	printf("%03.d\n", 99);

	printf("\nCase:\n%%01.d, 99\nOutput:\n");
	printf("%01.d\n", 99);

	printf("\nCase:\n%%5.0d, 0\nOutput:\n");
	printf("%5.0d\n", 0);

	printf("\nCase:\n%%5.3d, 99\nOutput:\n");
	printf("%5.3d\n", 99);

	printf("\nCase:\n%%5.1d, 99\nOutput:\n");
	printf("%5.1d\n", 99);

	printf("\nCase:\n%%2.3d, 99\nOutput:\n");
	printf("%2.3d\n", 99);

	printf("\nCase:\n%%2.3d, 9999\nOutput:\n");
	printf("%2.3d\n", 9999);

	return (0);
}
*/

#include <stdio.h>

int	main(void)
{
	printf("%09.7d\n", 12345);
	printf("%9.7d\n", 12345);
	printf("%#7x\n", 12345);
	return (0);
}



