d = {}
for i in range(int(input())):
    student_name = input()
    grade = float(input())
    if student_name not in d:
        d[student_name] = []
    d[student_name].append(grade)
d = {i: sum(d[i]) / len(d[i]) for i in d}
copy_d = {i: d[i] for i in d if d[i] >= 4.50}
sorted_copy_d = sorted(copy_d.items(), key=lambda x: x[1], reverse=True)
for i in sorted_copy_d:
    print(f'{i[0]} -> {i[1]:.2f}')