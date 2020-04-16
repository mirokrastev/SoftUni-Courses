#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main()
{
    double income, average_grade, minimum_wage;
    scanf("%lf%lf%lf", &income, &average_grade, &minimum_wage);
    bool min_scholar = false;
    bool excellence_scholar = false;
    double money_min_scholar = 0;
    double money_excellence_scholar = 0;

    if (income < minimum_wage){
        if (average_grade > 4.5){
            min_scholar = true;
            money_min_scholar = minimum_wage * 0.35;
        }
    }
    if (average_grade >= 5.5){
        excellence_scholar = true;
        money_excellence_scholar = average_grade * 25;
    }
    if (min_scholar && excellence_scholar){
        if (money_min_scholar > money_excellence_scholar){
            printf("You get a Social scholarship %.0f BGN", floor(money_min_scholar));
        }
        else if (money_min_scholar <= money_excellence_scholar){
            printf("You get a scholarship for excellent results %.0f BGN", floor(money_excellence_scholar));
        }
    }
    else if(min_scholar){
        printf("You get a Social scholarship %.0f BGN", floor(money_min_scholar));
    }
    else if(excellence_scholar){
        printf("You get a scholarship for excellent results %.0f BGN", floor(money_excellence_scholar));
    }
    else{
        printf("You cannot get a scholarship!");
    }
}