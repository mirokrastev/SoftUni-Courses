#include <stdio.h>
#include <stdlib.h>

int main()
{
    int hour_exam, min_exam, hour_arrival, min_arrival;
    scanf("%d %d %d %d", &hour_exam, &min_exam, &hour_arrival, &min_arrival);

    int total_exam_mins = hour_exam * 60 + min_exam;
    int total_arrival_mins = hour_arrival * 60 + min_arrival;

    int diff = total_exam_mins - total_arrival_mins;

    if (diff < 0){
        diff *= -1;
        if (diff >= 60)
        {
            int print_hours, print_mins;
            print_hours = diff / 60;
            print_mins = diff % 60;

            if (print_mins < 10)
            {
                printf("Late\n%d:0%d hours after the start", print_hours, print_mins);
            }
            else
            {
                printf("Late\n%d:%d hours after the start", print_hours, print_mins);
            }
        }
        else
        {
            printf("Late\n%d minutes after the start", diff);
        }
    }
    else {
        if (diff > 30)
        {
            if (diff >= 60)
            {
                int print_hours, print_mins;
                print_hours = diff / 60;
                print_mins = diff % 60;

                if (print_mins < 10)
                {
                    printf("Early\n%d:0%d hours before the start", print_hours, print_mins);
                }
                else
                {
                    printf("Early\n%d:%d hours before the start", print_hours, print_mins);
                }
            }
            else
            {
                printf("Early\n%d minutes before the start", diff);
            }
        }
        else
        {
            printf("On time\n%d minutes before the start", diff);
        }
    }
}