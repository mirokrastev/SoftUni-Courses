def student_record(student, grade):
    if student not in d:
        d[student] = []
    d[student].append(f'{grade:.2f}')


num = int(input())
d = {}

for i in range(num):
    student, grade = input().split()
    student_record(student, float(grade))

for k, v in d.items():
    avg = sum(map(float, v)) / len(v)
    print(f'{k} -> {" ".join(v)} (avg: {avg:.2f})')