import math

income = float(input())
grade = float(input())
min_salary = float(input())
social_scholarship = False
excellent_scholarship = False

if income < min_salary and grade >= 4.50:
    social_scholarship = True
    social_scholarship = min_salary * 0.35

if grade >= 5.50:
    excellent_scholarship = True
    excellent_scholarship = grade * 25

if social_scholarship and excellent_scholarship:
    if social_scholarship > excellent_scholarship:
        print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
elif social_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif excellent_scholarship:
    print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
else:
    print(f'You cannot get a scholarship!')