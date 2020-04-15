days_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
d = 0

for i in range(1, days_plunder+1):
    d += daily_plunder
    if i % 3 == 0:
        d += daily_plunder / 2
    if i % 5 == 0:
        d -= d * 0.3

if d >= expected_plunder:
    print(f'Ahoy! {d:.2f} plunder gained.')
else:
    print(f'Collected only {(d * 100) / expected_plunder:.2f}% of the plunder.')