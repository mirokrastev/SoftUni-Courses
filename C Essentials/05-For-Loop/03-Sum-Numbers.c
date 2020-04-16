#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    int sum = 0;
    scanf("%d", &num);

    for (int i = 1; i <= num; i++){
        int inp;
        scanf("%d", &inp);
        sum += inp;
    }

    printf("%d", sum);
}