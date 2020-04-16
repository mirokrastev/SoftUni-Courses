#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num_one, num_two;
    scanf("%d%d", &num_one, &num_two);

    if (num_one > num_two){
        printf("%d", num_one);
    }
    else{
        printf("%d", num_two);
    }
}