jury_count = int(input())

total_average = 0
presentations_count = 0
command = input()
while command != 'Finish':
    presentations_count += 1
    current_assessment_sum = 0
    for person in range(jury_count):
        current_assessment = float(input())
        current_assessment_sum += current_assessment

    current_average = current_assessment_sum / jury_count
    print(f'{command} - {current_average:.2f}.')
    total_average += current_average
    command = input()

average_assessment = total_average / presentations_count
print(f'Student\'s final assessment is {average_assessment:.2f}.')