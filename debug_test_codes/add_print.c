#include <stdio.h>

int main(void)
{
	int a = 3;
	int b, c = 2;
	asm("int3");
	b = a + c;
	printf("%d\n", b);
	return 0;
}