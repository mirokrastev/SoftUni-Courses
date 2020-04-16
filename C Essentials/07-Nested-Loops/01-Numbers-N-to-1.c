#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);

    for (int i = num; i > 0; i--){
        printf("%d\n", i);
    }
}