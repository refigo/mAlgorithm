#include <stdio.h>
#include <stdarg.h>

float	get_average(int count, ...)
{
	va_list	ap;
	int	sum;

	va_start(ap, count);
	sum = 0;
	for (int i = 0; i < count; i++)
	{
		sum += va_arg(ap, int);
	}
	va_end(ap);
	return ((float)sum / count);
}

int	main(void)
{
	printf("%.2f\n", get_average(2, 5, 7));
	printf("%.2f\n", get_average(6, 1, 2, 3, 4, 5, 6));
	return (0);
}
