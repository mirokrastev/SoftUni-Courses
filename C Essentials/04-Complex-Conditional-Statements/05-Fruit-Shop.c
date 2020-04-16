#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char fruit[15];
    char day[10];
    double quantity;
    double cena;
    scanf("%s %s %lf", fruit, day, &quantity);

    if (strcmp(day, "Saturday") == 0 || strcmp(day, "Sunday") == 0){
        if (strcmp(fruit, "banana") == 0){
            cena = 2.70;
        }
        else if (strcmp(fruit, "apple") == 0){
            cena = 1.25;
        }
        else if (strcmp(fruit, "orange") == 0){
            cena = 0.90;
        }
        else if (strcmp(fruit, "grapefruit") == 0){
            cena = 1.60;
        }
        else if (strcmp(fruit, "kiwi") == 0){
            cena = 3.00;
        }
        else if (strcmp(fruit, "pineapple") == 0){
            cena = 5.60;
        }
        else if (strcmp(fruit, "grapes") == 0){
            cena = 4.20;
        }
        else{
            printf("error");
            exit(0);
        }
    }
    else if (strcmp(day, "Monday") == 0 || strcmp(day, "Tuesday") == 0 || strcmp(day, "Wednesday") == 0
    || strcmp(day, "Thursday") == 0 || strcmp(day, "Friday") == 0){
        if (strcmp(fruit, "banana") == 0){
            cena = 2.50;
        }
        else if (strcmp(fruit, "apple") == 0){
            cena = 1.20;
        }
        else if (strcmp(fruit, "orange") == 0){
            cena = 0.85;
        }
        else if (strcmp(fruit, "grapefruit") == 0){
            cena = 1.45;
        }
        else if (strcmp(fruit, "kiwi") == 0){
            cena = 2.70;
        }
        else if (strcmp(fruit, "pineapple") == 0){
            cena = 5.50;
        }
        else if (strcmp(fruit, "grapes") == 0){
            cena = 3.85;
        }
        else{
            printf("error");
            exit(0);
        }
    }
    else{
        printf("error");
        exit(0);
    }
    printf("%.2f", cena * quantity);
}