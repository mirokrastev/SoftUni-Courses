years_count = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())
toys_count = 0
money_to_receive = 10
savings = 0

for year in range(1, years_count + 1):
    if year % 2 != 0:
        toys_count += 1
    else:
        savings += money_to_receive
        money_to_receive += 10
        savings -= 1

savings += toys_count * single_toy_price

if savings < washing_machine_price:
    diff = washing_machine_price - savings
    print(f'No! {diff:.2f}')
else:
    diff = savings - washing_machine_price
    print(f'Yes! {diff:.2f}')