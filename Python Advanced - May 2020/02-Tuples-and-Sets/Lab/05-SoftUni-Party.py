num_guests = int(input())
vip_guests = set()
regular_guests = set()


def add_guests(guest):
    vip_guests.add(guest) if guest[0].isdigit() else regular_guests.add(guest)


def remove_guests(guest):
    if guest in vip_guests:
        vip_guests.remove(guest)
    else:
        regular_guests.remove(guest)


def print_guests(*guests):
    print(len(vip_guests.union(regular_guests)))
    for i in sorted(guests[0]):
        print(i)

    for i in sorted(guests[1]):
        print(i)


for i in range(num_guests):
    guest = input()
    add_guests(guest)

while True:
    arg = input()
    if arg == 'END':
        print_guests(vip_guests, regular_guests)
        break
    else:
        remove_guests(arg)