#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int width, length, height;
    scanf("%d %d %d", &width, &length, &height);
    int total = width * length * height;

    while (1){
        if (total < 0){
            printf("No more free space! You need %d Cubic meters more.", abs(total));
            return 0;
        }
        char inp[20];
        scanf("%s", inp);

        if (strcmp(inp, "Done") == 0){
            printf("%d Cubic meters left.", total);
            return 0;
        }
        else{
            int space = atoi(inp);
            total -= space;
        }
    }
}