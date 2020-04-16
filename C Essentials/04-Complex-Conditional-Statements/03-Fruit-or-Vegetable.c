#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char inp[15];
    scanf("%s", inp);

    if (strcmp(inp, "banana") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "apple") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "cherry") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "lemon") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "grapes") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "kiwi") == 0){
        printf("fruit");
    }
    else if (strcmp(inp, "tomato") == 0){
        printf("vegetable");
    }
    else if (strcmp(inp, "cucumber") == 0){
        printf("vegetable");
    }
    else if (strcmp(inp, "pepper") == 0){
        printf("vegetable");
    }
    else if (strcmp(inp, "carrot") == 0){
        printf("vegetable");
    }
    else{
        printf("unknown");
    }
}