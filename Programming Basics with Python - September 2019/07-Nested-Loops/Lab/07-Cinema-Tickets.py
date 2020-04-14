standard_tickets_count = 0
kid_tickets_count = 0
student_tickets_count = 0
total_seats_taken = 0
movie = input()
while movie != 'Finish':
    free_seats = int(input())
    taken_seats = 0
    for seat in range(free_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        taken_seats += 1
        if ticket_type == 'student':
            student_tickets_count += 1
        elif ticket_type == 'standard':
            standard_tickets_count += 1
        elif ticket_type == 'kid':
            kid_tickets_count += 1

    total_seats_taken += taken_seats
    percent_taken = taken_seats / free_seats * 100
    print(f'{movie} - {percent_taken:.2f}% full.')
    movie = input()

print(f'Total tickets: {total_seats_taken}')
students_percentage = student_tickets_count / total_seats_taken * 100
standard_percentage = standard_tickets_count / total_seats_taken * 100
kids_percentage = kid_tickets_count / total_seats_taken * 100
print(f'{students_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kids_percentage:.2f}% kids tickets.')