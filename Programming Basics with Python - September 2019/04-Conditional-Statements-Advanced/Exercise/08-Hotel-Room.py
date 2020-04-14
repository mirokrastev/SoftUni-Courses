month = input()
stay_night = int(input())

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if stay_night > 14:
        studio *= 0.7
        apartment *= 0.9
    elif stay_night > 7:
        studio *= 0.95
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if stay_night > 14:
        studio *= 0.8
        apartment *= 0.9
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if stay_night > 14:
        apartment *= 0.9
total_sum_st = studio * stay_night
total_sum_ap = apartment * stay_night
print(f'Apartment: {total_sum_ap:.2f} lv.\nStudio: {total_sum_st:.2f} lv.')