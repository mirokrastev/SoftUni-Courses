whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakija_liters = float(input())
whiskey_liters = float(input())

rakija_price = whiskey_price / 2
wine_price = rakija_price - (rakija_price * 0.4)
beer_price = rakija_price * 0.2

rakija_total = rakija_price * rakija_liters
wine_total = wine_liters * wine_price
beer_total = beer_liters * beer_price
whiskey_total = whiskey_price * whiskey_liters

total_sum = rakija_total + wine_total + beer_total + whiskey_total

print(f'{total_sum:.2f}')