steps_made = int(input())
length_one_step = float(input())
distance_to_travel = int(input()) * 100
d = 0

for i in range(1, steps_made+1):
    if i % 5 == 0:
        d += length_one_step * 0.7
        continue
    d += length_one_step

print(f'You travelled {(d*100)/distance_to_travel:.2f}% of the distance!')