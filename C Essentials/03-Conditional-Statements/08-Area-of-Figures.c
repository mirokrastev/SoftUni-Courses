#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char type[9];
    scanf("%s", type);

    if (strcmp(type, "square") == 0){
        double num;
        scanf("%lf", &num);

        printf("%.3f", num * num);
    }
    else if (strcmp(type, "rectangle") == 0){
        double num_one, num_two;
        scanf("%lf%lf", &num_one, &num_two);

        printf("%.3f", num_one * num_two);
    }
    else if (strcmp(type, "circle") == 0){
        double num;
        scanf("%lf", &num);

        printf("%.3f", 3.14159265359 * (num* num));
    }
    else if (strcmp(type, "triangle") == 0){
        double num_one, num_two;
        scanf("%lf%lf", &num_one, &num_two);

        printf("%.3f", 0.5 * num_one * num_two);
    }
}