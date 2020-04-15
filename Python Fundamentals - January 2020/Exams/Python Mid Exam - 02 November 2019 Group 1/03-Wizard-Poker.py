old_deck = input().split(':')
new_deck = []

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Ready':
        print(*new_deck, sep=' ')
        exit()
    if command == 'Add':
        card_name = cmd[1]
        if card_name in old_deck:
            new_deck.append(card_name)
            old_deck.remove(card_name)
        else:
            print('Card not found.')
    elif command == 'Insert':
        card_name = cmd[1]
        index = int(cmd[2])
        if all([index <= len(new_deck) - 1, index >= 0, card_name in old_deck]):
            new_deck.insert(index, card_name)
            old_deck.remove(card_name)
        else:
            print('Error!')
    elif command == 'Remove':
        card_name = cmd[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print('Card not found.')
    elif command == 'Swap':
        card_one = cmd[1]
        card_two = cmd[2]
        new_deck[new_deck.index(card_two)], new_deck[new_deck.index(card_one)] = \
            new_deck[new_deck.index(card_one)], new_deck[new_deck.index(card_two)]
    elif command == 'Shuffle':
        new_deck.reverse()