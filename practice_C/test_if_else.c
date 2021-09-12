#include <stdio.h>
#include <stdlib.h>

static int	itoa_size(long long ll_n, int size)
{
	if (0 == ll_n)
		return (1);
	if (ll_n < 0)
	{
		size++;
		ll_n *= -1;
	}
	while (ll_n)
	{
		size++;
		ll_n /= 10;
	}
	return (size);
}

char	*ft_itoa(int n)
{
	char		*ret;
	int			size;
	long long	ll_n;

	ll_n = (long long)n;
	size = itoa_size(ll_n, 0);
	ret = (char *)malloc(size + 1);
	if (!ret)
		return (NULL);
	ret[size--] = '\0';
	if (0 == ll_n)
		ret[0] = '0';
	if (ll_n < 0)
		ll_n *= -1;
	else
		ll_n *= 1;
	printf("ll_n is %lld\n", ll_n);
	while (ll_n)
	{
		ret[size--] = ('0' + (ll_n % 10));
		ll_n /= 10;
	}
	if (n < 0)
		ret[size] = '-';
	return (ret);
}

int	main(void)
{
	char	*s1;
	char	*s2;
	
	s1 = ft_itoa(-2147483648);
	s2 = ft_itoa(2147483647);
	printf("%s\n", s1);
	printf("%s\n", s2);
	return (0);
}

