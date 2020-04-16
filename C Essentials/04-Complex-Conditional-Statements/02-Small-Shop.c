#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char product[10];
    char city[10];
    double quantity;

    scanf("%s%s%lf", product, city, &quantity);

    if (strcmp(city, "Sofia") == 0){
        if (strcmp(product, "coffee") == 0){
            printf("%g", quantity * 0.5);
        }
        else if (strcmp(product, "water") == 0){
            printf("%g", quantity * 0.8);
        }
        else if (strcmp(product, "beer") == 0){
            printf("%g", quantity * 1.20);
        }
        else if (strcmp(product, "sweets") == 0){
            printf("%g", quantity * 1.45);
        }
        else if (strcmp(product, "peanuts") == 0){
            printf("%g", quantity * 1.60);
        }
    }
    else if (strcmp(city, "Plovdiv") == 0){
        if (strcmp(product, "coffee") == 0){
            printf("%g", quantity * 0.4);
        }
        else if (strcmp(product, "water") == 0){
            printf("%g", quantity * 0.7);
        }
        else if (strcmp(product, "beer") == 0){
            printf("%g", quantity * 1.15);
        }
        else if (strcmp(product, "sweets") == 0){
            printf("%g", quantity * 1.30);
        }
        else if (strcmp(product, "peanuts") == 0){
            printf("%g", quantity * 1.50);
        }
    }
    else if (strcmp(city, "Varna") == 0){
        if (strcmp(product, "coffee") == 0){
            printf("%g", quantity * 0.45);
        }
        else if (strcmp(product, "water") == 0){
            printf("%g", quantity * 0.7);
        }
        else if (strcmp(product, "beer") == 0){
            printf("%g", quantity * 1.10);
        }
        else if (strcmp(product, "sweets") == 0){
            printf("%g", quantity * 1.35);
        }
        else if (strcmp(product, "peanuts") == 0){
            printf("%g", quantity * 1.55);
        }
    }
}