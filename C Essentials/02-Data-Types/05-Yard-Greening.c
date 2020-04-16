#include <stdio.h>
#include <stdlib.h>

int main()
{
    double price_per_square_m = 7.61;
    double square_meters;
    scanf("%lf", &square_meters);
    double total_raw = square_meters * price_per_square_m;
    double total = (square_meters * price_per_square_m) * 0.82;
    printf("The final price is: %.2f lv.\n", total);
    printf("The discount is: %.2f lv.", total_raw - total);
}