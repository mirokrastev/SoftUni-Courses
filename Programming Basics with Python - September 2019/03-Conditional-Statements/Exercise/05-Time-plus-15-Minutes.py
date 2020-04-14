hours = int(input())
minutes = int(input())

hours_as_mins = hours * 60
total_mins = hours_as_mins + minutes + 15

final_hours = total_mins // 60
final_mins = total_mins % 60

if final_hours == 24:
    final_hours = 0

if final_mins < 10:
    print(f'{final_hours}:0{final_mins}')
else:
    print(f'{final_hours}:{final_mins}')