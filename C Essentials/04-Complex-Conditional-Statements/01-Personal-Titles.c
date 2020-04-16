#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    double age;
    char gender;

    scanf("%lf %c", &age, &gender);

    if (gender == 'm'){
        if (age < 16){
            printf("Master");
        }
        else if (age >= 16){
            printf("Mr.");
        }
    }
    else if (gender == 'f'){
        if (age < 16){
            printf("Miss");
        }
        else if (age >= 16){
            printf("Ms.");
        }
    }
}