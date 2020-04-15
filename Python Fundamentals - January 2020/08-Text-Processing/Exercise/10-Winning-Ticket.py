def if_win(ticket):
    left_half = ticket[0:10]
    right_half = ticket[10:20]
    combination = ''
    win = False
    symbol = None
    for s in winning_symbols:
        combination = ''
        for i in range(6):
            combination += s
        if combination in left_half and combination in right_half:
            win = True
            symbol = s
            break
    return [win, symbol]


def count_s(ticket, s):
    left_half = list(ticket[0:10])
    right_half = list(ticket[10:20])
    lc = left_half.count(s)
    rc = right_half.count(s)
    return min([lc, rc])


tickets = input().split(',')
winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    ticket = ticket.split()[0]
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    if if_win(ticket)[0]:
        if count_s(ticket, if_win(ticket)[1]) == 10:
            print(f'ticket "{ticket}" - {10}{if_win(ticket)[1]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {count_s(ticket, if_win(ticket)[1])}{if_win(ticket)[1]}')
    else:
        print(f'ticket "{ticket}" - no match')