#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[20];
    scanf("%s", name);
    double grades = 0;
    int classes = 1;
    int expel = 0;

    while (classes != 13){
        if (expel == 2){
            printf("%s has been excluded at %d grade", name, classes);

            return 0;
        }
        double grade_class;
        scanf("%lf", &grade_class);

        if (grade_class >= 4.00){
            grades += grade_class;
            classes += 1;
        }
        else{
            expel += 1;
        }
    }
    printf("%s graduated. Average grade: %.2f", name, grades / 12);
}