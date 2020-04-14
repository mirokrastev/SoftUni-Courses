name = input()
level = 1
sum_grades = 0

while level <= 12:
    grade = float(input())

    if grade >= 4:
        level += 1
        sum_grades += grade

print(f'{name} graduated. Average grade: {(sum_grades / 12):.2f}')