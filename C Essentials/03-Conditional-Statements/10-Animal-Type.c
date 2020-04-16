#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char ebane[30];
    scanf("%s", ebane);

    if (strcmp(ebane, "dog") == 0){
        printf("mammal");
    }
    else if (strcmp(ebane, "snake") == 0){
        printf("reptile");
    }
    else if (strcmp(ebane, "crocodile") == 0){
        printf("reptile");
    }
    else if (strcmp(ebane, "tortoise") == 0){
        printf("reptile");
    }
    else{
        printf("unknown");
    }
}