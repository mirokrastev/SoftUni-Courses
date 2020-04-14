days_spent = int(input())
room_type = input()
feedback = input()
nights_spent = days_spent - 1

discount = 0
price = 0

if room_type == 'apartment':
    price = 25
    if nights_spent < 10:
        discount = 0.3
    elif 10 <= nights_spent <= 15:
        discount = 0.35
    elif nights_spent > 15:
        discount = 0.5
elif room_type == 'president apartment':
    price = 35
    if nights_spent < 10:
        discount = 0.1
    elif 10 <= nights_spent <= 15:
        discount = 0.15
    elif nights_spent > 15:
        discount = 0.2
elif room_type == 'room for one person':
    price = 18

total_sum = nights_spent * price
total_sum -= total_sum * discount

if feedback == 'positive':
    total_sum += total_sum * 0.25
elif feedback == 'negative':
    total_sum -= total_sum * 0.1

print(f'{total_sum:.2f}')