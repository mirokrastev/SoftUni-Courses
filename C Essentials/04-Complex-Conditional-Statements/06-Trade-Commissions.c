#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char town[15];
    double sales_volume, commission;
    scanf("%s %lf", town, &sales_volume);

    if (0 <= sales_volume && sales_volume <= 500){
        if (strcmp(town, "Sofia") == 0){
            commission = 0.05;
        }
        else if (strcmp(town, "Varna") == 0){
            commission = 0.045;
        }
        else if (strcmp(town, "Plovdiv") == 0){
            commission = 0.055;
        }
        else {
            printf("error");
            exit(0);
        }
    }
    else if (500 <= sales_volume && sales_volume <= 1000){
        if (strcmp(town, "Sofia") == 0){
            commission = 0.07;
        }
        else if (strcmp(town, "Varna") == 0){
            commission = 0.075;
        }
        else if (strcmp(town, "Plovdiv") == 0){
            commission = 0.08;
        }
        else {
            printf("error");
            exit(0);
        }
    }
    else if (1000 <= sales_volume && sales_volume <= 10000){
        if (strcmp(town, "Sofia") == 0){
            commission = 0.08;
        }
        else if (strcmp(town, "Varna") == 0){
            commission = 0.1;
        }
        else if (strcmp(town, "Plovdiv") == 0){
            commission = 0.12;
        }
        else {
            printf("error");
            exit(0);
        }
    }
    else if (sales_volume > 10000){
        if (strcmp(town, "Sofia") == 0){
            commission = 0.12;
        }
        else if (strcmp(town, "Varna") == 0){
            commission = 0.13;
        }
        else if (strcmp(town, "Plovdiv") == 0){
            commission = 0.145;
        }
        else {
            printf("error");
            exit(0);
        }
    }
    else {
        printf("error");
        exit(0);
    }
    printf("%.2f", sales_volume * commission);
}