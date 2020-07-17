from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        rooms = [room for room in self.rooms if room.number == room_number]
        if not rooms: return

        room = rooms[0]

        if room.is_taken:
            return

        if room.guests + people > room.capacity:
            return

        room.guests += people
        room.is_taken = True
        self.guests += people

    def free_room(self, room_number):
        rooms = [room for room in self.rooms if room.number == room_number]
        if not rooms: return

        room = rooms[0]

        self.guests -= room.guests
        room.guests = 0
        room.is_taken = False

    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]

        print(f'Hotel {self.name} has {len(self.rooms)} total guests')
        if free_rooms:
            print(f'Free rooms: {", ".join(map(str, free_rooms))}')
        if taken_rooms:
            print(f'Taken rooms: {", ".join(map(str, taken_rooms))}')