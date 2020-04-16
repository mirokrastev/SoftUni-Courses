#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int width, length;
    scanf("%d %d", &width, &length);
    int total = width * length;

    while (1){
        if (total < 0){
            printf("No more cake left! You need %d pieces more.", abs(total));
            return 0;
        }
        char cake[20];
        scanf("%s", &cake);

        if (strcmp(cake, "STOP") == 0){
            printf("%d pieces are left.", total);
            return 0;
        }
        else{
            int num = atoi(cake);
            total -= num;
        }
    }
}