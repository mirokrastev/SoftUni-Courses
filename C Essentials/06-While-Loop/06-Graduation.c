#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[20];
    scanf("%s", name);
    double grades = 0;
    int classes = 0;

    while (classes != 12){
        double grade_class;
        scanf("%lf", &grade_class);

        if (grade_class >= 4.00){
            grades += grade_class;
            classes += 1;
        }
    }
    printf("%s graduated. Average grade: %.2f", name, grades / 12);
}