records = {}
 
for _ in range(int(input())):
    (name, grade) = input().split(" ")
    if name not in records:
        records[name] = []
    records[name].append(f'{float(grade):.2f}')
 
for key, value in records.items():
    print(f'{key} -> {" ".join(value)} (avg: {(sum(map(float, value)) / len(value)):.2f})')