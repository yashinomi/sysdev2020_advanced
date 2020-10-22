#include <stdio.h>

int main(int argc, char const *argv[]){
    printf("%d\n", *(int*)(NULL));
    return 0;
}
