#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{
    int num;
    scanf("%d", &num);
    int biggest = INT_MIN;
    int smallest = INT_MAX;

    for (int i = 1; i <= num; i++){
        int inp;
        scanf("%d", &inp);

        if (inp > biggest){
            biggest = inp;
        }
        if (inp < smallest){
            smallest = inp;
        }
    }

    printf("Max number: %d\n", biggest);
    printf("Min number: %d\n", smallest);
}