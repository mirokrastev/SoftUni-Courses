class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.guests = []

    def add_guest(self, person):
        self.guests.append(person)

    def get_summary(self):
        guest_names = ', '.join([guest.name for guest in self.guests])
        return f'Going: {guest_names}\nTotal: {len(self.guests)}'


party = Party()


while True:
    command = input()
    if command == 'End':
        break
    person_name = command
    person = Person(person_name)
    party.add_guest(person)

print(party.get_summary())