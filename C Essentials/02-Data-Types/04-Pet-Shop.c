#include <stdio.h>
#include <stdlib.h>

int main()
{
    double zoo_price = 2.50;
    int my_dog_price = 4;
    int zoo_dog_c;
    int my_dog_c;
    scanf("%d%d", &zoo_dog_c, &my_dog_c);
    double total = (zoo_price * zoo_dog_c) + (my_dog_price * my_dog_c);
    printf("%.2f lv.", total);
}