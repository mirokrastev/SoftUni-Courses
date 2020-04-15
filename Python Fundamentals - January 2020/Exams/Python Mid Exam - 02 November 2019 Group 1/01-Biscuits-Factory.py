import math
amount_biscuit_per_worker = int(input())
count_workers = int(input())
comp_fact_biscuits = int(input())
produced_biscuits_my_comp = 0

for i in range(1, 31):
    if i % 3 == 0:
        produced_biscuits_my_comp += math.floor((amount_biscuit_per_worker * count_workers) * 0.75)
        continue
    produced_biscuits_my_comp += math.floor(amount_biscuit_per_worker * count_workers)
print(f'You have produced {produced_biscuits_my_comp} biscuits for the past month.')
d = produced_biscuits_my_comp - comp_fact_biscuits
if d > 0:
    print(f'You produce {(d/comp_fact_biscuits) * 100:.2f} percent more biscuits.')
else:
    d = abs(d)
    print(f'You produce {(d/comp_fact_biscuits) * 100:.2f} percent less biscuits.')