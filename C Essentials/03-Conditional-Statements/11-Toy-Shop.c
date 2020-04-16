#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    double puzzle = 2.60;
    double doll = 3.00;
    double teddy_bear = 4.10;
    double minion = 8.20;
    double truck = 2.00;

    double vacation_price;
    double puzzle_count, dolls_count, teddy_count, minion_count, truck_count;

    scanf("%lf", &vacation_price);
    scanf("%lf%lf%lf%lf%lf", &puzzle_count, &dolls_count, &teddy_count, &minion_count, &truck_count);

    double toys_count = puzzle_count + dolls_count + teddy_count + minion_count + truck_count;
    double sum_raw = (puzzle_count * puzzle) + (dolls_count * doll) + (teddy_count * teddy_bear)
            + (minion_count * minion) + (truck_count * truck);
    if (toys_count >= 50){
        sum_raw *= 0.75;
    }
    sum_raw = (sum_raw * 0.9);
    if (sum_raw >= vacation_price){
        sum_raw -= vacation_price;
        printf("Yes! %.2f lv left.", sum_raw);
    }
    else {
        printf("Not enough money! %.2f lv needed.", vacation_price - sum_raw);
    }
}