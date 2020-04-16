#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int first;
    scanf("%d", &first);
    int second;
    scanf("%d", &second);
    double H;
    H = sqrt(first*first + second*second);
    printf("Hypotenuse is %d.", (int) H);
}