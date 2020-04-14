exam_hours = int(input())
exam_mins = int(input())
arrival_hours = int(input())
arrival_mins = int(input())

total_exam_mins = exam_hours * 60 + exam_mins
total_arrival_mins = arrival_hours * 60 + arrival_mins

diff = total_exam_mins - total_arrival_mins

if diff < 0:
    diff *= -1
    if diff >= 60:
        print_hours = diff // 60
        print_mins = diff % 60

        if print_mins < 10:
            print(f'Late\n{print_hours}:0{print_mins} hours after the start')
        else:
            print(f'Late\n{print_hours}:{print_mins} hours after the start')
    else:
        print(f'Late\n{diff} minutes after the start')
else:
    if diff > 30:
        if diff >= 60:
            print_hours = diff // 60
            print_mins = diff % 60

            if print_mins < 10:
                print(f'Early\n{print_hours}:0{print_mins} hours before the start')
            else:
                print(f'Early\n{print_hours}:{print_mins} hours before the start')
        else:
            print(f'Early\n{diff} minutes before the start')
    else:
        print(f'On time\n{diff} minutes before the start')