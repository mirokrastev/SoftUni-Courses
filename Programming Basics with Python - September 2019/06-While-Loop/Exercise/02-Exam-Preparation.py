poor_grades_threshold = int(input())
exercises_counter = 0
poor_grades_counter = 0
grades_sum = 0
last_exercise = None

while poor_grades_counter < poor_grades_threshold:
    exercise = input()
    if exercise == 'Enough':
        print(f'Average score: {(grades_sum / exercises_counter):.2f}')
        print(f'Number of problems: {exercises_counter}')
        print(f'Last problem: {last_exercise}')
        break
    grade = int(input())
    if grade <= 4:
        exercises_counter += 1
        poor_grades_counter += 1
        grades_sum += grade
        last_exercise = exercise
    elif grade > 4:
        exercises_counter += 1
        grades_sum += grade
        last_exercise = exercise

if poor_grades_counter == poor_grades_threshold:
    print(f'You need a break, {poor_grades_counter} poor grades.')