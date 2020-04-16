#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int sum = 0;
    char var[30];
    while (1){
        char name[30];
        int sum_var = 0;
        scanf("%s", name);

        if (strcmp(name, "STOP") == 0){
            break;
        }

        for (int i = 0; i < strlen(name); i++){
            sum_var += name[i];
        }
        if (sum_var > sum){
            sum = sum_var;
            strcpy(var, name);
        }
    }
    printf("Winner is %s - %d!", var, sum);
}