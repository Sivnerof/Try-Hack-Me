#include <unistd.h>
int main()
{
	char str[13];
	int s;
	s=read(0, str, 13);
	write(1, str, s);
	return 0;
}
