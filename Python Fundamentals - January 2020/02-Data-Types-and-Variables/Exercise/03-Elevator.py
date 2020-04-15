import math
n_persons = int(input())
p_capacity = int(input())
courses = math.ceil(n_persons / p_capacity)
print(courses)