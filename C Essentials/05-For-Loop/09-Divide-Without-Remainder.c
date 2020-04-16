#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    double p1 = 0, p2 = 0, p3 = 0;
    scanf("%d", &x);

    for (int i = 0; i < x; i++){
        int num;
        scanf("%d", &num);

        if (num % 2 == 0){
            p1 += 1;
        }
        if (num % 3 == 0){
            p2 += 1;
        }
        if (num % 4 == 0){
            p3 += 1;
        }
    }

    p1 = p1 / x * 100;
    p2 = p2 / x * 100;
    p3 = p3 / x * 100;

    printf("%.2f%%\n", p1);
    printf("%.2f%%\n", p2);
    printf("%.2f%%\n", p3);
}