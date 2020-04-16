#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);

    int even = 0, odd = 0;

    for (int i = 1; i <= num; i++){
        int inp;
        scanf("%d", &inp);

        if (i % 2 == 0){
            even += inp;
        }
        else{
            odd += inp;
        }
    }

    if (even == odd){
        printf("Yes\nSum = %d", even);
    }
    else{
        printf("No\nDiff = %d", abs(even - odd));
    }
}