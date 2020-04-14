name = input()
classes_counter = 1
sum_grades = 0
bad_grades = 1

while classes_counter <= 12:
    if bad_grades > 2:
        print(f'{name} has been excluded at {classes_counter} grade')
        exit()

    grade = float(input())
    if grade >= 4:
        classes_counter += 1
        sum_grades += grade
    elif grade < 4:
        bad_grades += 1

print(f'{name} graduated. Average grade: {(sum_grades / 12):.2f}')