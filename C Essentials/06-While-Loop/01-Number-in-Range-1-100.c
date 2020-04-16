#include <stdio.h>
#include <stdlib.h>

int main()
{
    while (1){
        int num;
        scanf("%d", &num);

        if (1 <= num && num <= 100){
            printf("The num is: %d", num);

            return 0;
        }
        else{
            printf("Invalid number!\n");
        }
    }
}