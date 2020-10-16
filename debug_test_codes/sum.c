#include <stdlib.h>
#include <stdio.h>


int main(int argc, char const *argv[]){
    int sum = 0;
    int beg = atoi(argv[1]);
    int end = atoi(argv[2]);

    for (int i = beg; i <= end; i++){
        sum += i;
    }
	printf("%d\n", sum);
	return 0;
}