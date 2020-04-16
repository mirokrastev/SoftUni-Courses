#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char dest[256];
    scanf("%99[^\n]", dest);

    while(strcmp(dest, "End") != 0) {
        double money_needed, savings = 0;
        scanf("%lf", &money_needed);

        while(savings < money_needed) {
            double current_sum;
            scanf("%lf", &current_sum);
            savings += current_sum;
        }
        printf("Going to %s!\n", dest);
        scanf("%s", dest);
        scanf("%99[^\n]", dest);
    }
}