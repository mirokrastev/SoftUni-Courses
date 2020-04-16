#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);
    int max_num = 999999999;

    for (int i = 0; i < num; i++){
        int number;
        scanf("%d", &number);

        if (number < max_num){
            max_num = number;
        }
    }
    printf("%d", max_num);
}