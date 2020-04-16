#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char ebane[50];
    gets(ebane);

    if (strcmp(ebane, "s3cr3t!P@ssw0rd") == 0){
        printf("Welcome");
    }
    else{
        printf("Wrong password!");
    }
}