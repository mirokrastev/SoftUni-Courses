x = int(input())
salary = int(input())

for i in range(x):
    site = input()

    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50

    salary = max(salary, 0)
    if salary == 0:
        break
if salary == 0:
    print('You have lost your salary.')
else:
    print(salary)