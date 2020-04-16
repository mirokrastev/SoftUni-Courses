#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);
    int var = 0;

    while (1){
        if (var * 2 + 1 > num){
            return 0;
        }
        else{
            var = (var * 2) + 1;
            printf("%d\n", var);
        }
    }
}