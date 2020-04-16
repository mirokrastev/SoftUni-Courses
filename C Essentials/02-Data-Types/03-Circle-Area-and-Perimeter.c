#include <stdio.h>
#include <stdlib.h>

int main()
{
    double inp;
    scanf("%lf", &inp);
    double area = 3.14159265359 * inp * inp;
    double perimeter = 2 * 3.14159265359 * inp;
    printf("%.2f\n", area);
    printf("%.2f", perimeter);
}