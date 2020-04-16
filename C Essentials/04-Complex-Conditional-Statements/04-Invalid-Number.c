#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int num;
    scanf("%d", &num);

    if ((num >= 100 && num <= 200) || num == 0){
        return 0;
    }
    else{
        printf("invalid");
    }
}