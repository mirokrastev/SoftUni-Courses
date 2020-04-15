size_of_side = float(input())
number_sheets_paper = int(input())
area_single_sheet = float(input())
area_gift_box = size_of_side * size_of_side * 6
d = 0

for i in range(1, number_sheets_paper+1):
    if i % 3 == 0:
        d += area_single_sheet * 0.25
    else:
        d += area_single_sheet

print(f'You can cover {(d / area_gift_box) * 100:.2f}% of the box.')