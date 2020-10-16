#include <stdlib.h>
#include <stdio.h>

int collatz(int n) {
	if (n == 1) return 1;
	if (n % 2) return collatz(3 * n + 1);
	else return collatz(n / 2);
}


int main(int argc, char const *argv[]){
	printf("%d\n", collatz(atoi(argv[1])));
	return 0;
}