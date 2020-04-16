#include <stdio.h>
#include <stdlib.h>

int main()
{
    int floor, room;
    scanf("%d %d", &floor, &room);

    for (int i = floor; i > 0; i--){
        if (i == floor){
            for (int l = 0; l < room; l++){
                printf("L%d%d ", i, l);
            }
        }
        else if (i % 2 == 0){
            printf("\n");
            for (int l = 0; l < room; l++){
                printf("O%d%d ", i, l);
            }
        }
        else{
            printf("\n");
            for (int l = 0; l < room; l++){
                printf("A%d%d ", i, l);
            }
        }
    }
}