#include <stdio.h>
#include <stdlib.h>

int main()
{
    int length, width, height;
    double percent;
    scanf("%d%d%d%lf", &length, &width, &height, &percent);
    double total_raw = length * width * height;
    double percent_total = percent * 0.01;
    double total = total_raw * 0.001;
    printf("%.3f", total * (1-percent_total));
}