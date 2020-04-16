#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);
    int diff_one = 0, diff_two = 0;

    for (int i = 1; i <= num; i++){
        int inp;
        scanf("%d", &inp);
        diff_one += inp;
    }

    for (int i = 1; i <= num; i++){
        int inp;
        scanf("%d", &inp);
        diff_two += inp;
    }

    if (diff_one == diff_two){
        printf("Yes, sum = %d", diff_one);
    }
    else{
        printf("No, diff = %d", abs(diff_one - diff_two));
    }
}