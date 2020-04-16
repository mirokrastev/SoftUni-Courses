#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int day_vacation;
    char room_type[40];
    char evaluation[10];

    double room_person = 18.00;
    double apartment = 25.00;
    double president_ap = 35.00;
    double discount;

    scanf("%d\n", &day_vacation);
    gets(room_type);
    scanf("%s", evaluation);
    day_vacation -= 1;

    if (strcmp(room_type, "room for one person") == 0){
        if (strcmp(evaluation, "positive") == 0){
            printf("%.2f", (room_person * day_vacation) * 1.25);
        }
        else if (strcmp(evaluation, "negative") == 0){
            printf("%.2f", (room_person * day_vacation) * 0.9);
        }
    }
    else if (strcmp(room_type, "apartment") == 0){
        if (day_vacation < 10){
            discount = 0.7;
        }
        else if (day_vacation >= 10 && day_vacation < 15){
            discount = 0.65;
        }
        else if (day_vacation > 15){
            discount = 0.5;
        }
        if (strcmp(evaluation, "positive") == 0){
            printf("%.2f", ((apartment * day_vacation) * discount) * 1.25);
        }
        else if (strcmp(evaluation, "negative") == 0){
            printf("%.2f", ((apartment * day_vacation) * discount) * 0.9);
        }
    }
    else if (strcmp(room_type, "president apartment") == 0){
        if (day_vacation < 10){
            discount = 0.9;
        }
        else if (day_vacation >= 10 && day_vacation < 15){
            discount = 0.85;
        }
        else if (day_vacation > 15){
            discount = 0.8;
        }
        if (strcmp(evaluation, "positive") == 0){
            printf("%.2f", ((president_ap * day_vacation) * discount) * 1.25);
        }
        else if (strcmp(evaluation, "negative") == 0){
            printf("%.2f", ((president_ap * day_vacation) * discount) * 0.9);
        }
    }
}