#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);
    int var = 1;

    for (int i = 0; i < num+1; i += 2){
        printf("%d\n", var);
        var *= 2 * 2;
    }
}