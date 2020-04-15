employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
people_count = int(input())
hours = 0

while people_count >= 0:
    if people_count <= 0:
        break
    hours += 1
    if hours % 4 == 0:
        continue
    all = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
    people_count -=  all

print(f'Time needed: {hours}h.')