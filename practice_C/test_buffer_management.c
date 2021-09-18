#include <stdio.h>
#include <unistd.h>

int main(void)
{
	char	*test;

	test = "segfaulterino";
	printf("worldi ");
	//printf("world\n");
	write(1, "hello ", 6);
	test[0] = 'b';
	return (0);
}
