trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = puzzles_count * 2.6 + dolls_count * 3 + teddy_bears_count * 4.10 + minions_count * 8.20 + trucks_count * 2
total_toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if total_toys_count >= 50:
    total_price -= total_price * 0.25

total_price -= total_price * 0.10

left_money = trip_price - total_price

if left_money > 0:
    print(f"Not enough money! {left_money:.2f} lv needed.")
else:
    print(f"Yes! {abs(left_money):.2f} lv left.")