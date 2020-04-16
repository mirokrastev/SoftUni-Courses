#include <stdio.h>
#include <stdlib.h>

int main()
{
    int cake = 45;
    double waffles = 5.80;
    double pancakes = 3.20;
    int campaign_days, workers_count, cakes_count, waffles_count, pancakes_count;

    scanf("%d%d%d%d%d", &campaign_days, &workers_count, &cakes_count, &waffles_count, &pancakes_count);

    double cakes_total = cakes_count * cake;
    double waffles_total = waffles_count * waffles;
    double pancakes_total = pancakes_count * pancakes;
    double amount_per_day = (cakes_total + waffles_total + pancakes_total) * workers_count;
    double amount_whole_camp = amount_per_day * campaign_days;

    printf("%.2f", amount_whole_camp * 0.875);
}