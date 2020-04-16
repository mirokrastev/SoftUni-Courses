#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age, toy_price, toys = 0, saved_money = 0;
    double washing_m_price;

    scanf("%d", &age);
    scanf("%lf", &washing_m_price);
    scanf("%d", &toy_price);
    int money = 0;
    int to_take = 0;

    for (int i = 1; i <= age; i++){
        if (i % 2 == 1){
            toys += 1;
        }
        else{
            money += 10;
            to_take += 1;
            saved_money += money;
        }
    }

    saved_money += (toys * toy_price) - to_take;
    if (saved_money >= washing_m_price){
        printf("Yes! %.2f", saved_money - washing_m_price);
    }
    else{
        printf("No! %.2f", washing_m_price - saved_money);
    }
}