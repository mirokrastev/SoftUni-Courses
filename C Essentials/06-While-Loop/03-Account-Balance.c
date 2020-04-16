#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int contributions;
    scanf("%d", &contributions);
    double total = 0;

    for (int i = 0; i < contributions; i++){
        double increase;
        scanf("%lf", &increase);

        if (increase < 0){
            printf("Invalid operation!\n");
            printf("Total: %.2f\n", total);

            return 0;
        }
        else{
            total += increase;
            printf("Increase: %.2f\n", increase);
        }
    }
    printf("Total: %.2f\n", total);
}