from project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats: int, rows: int, seats_per_row: int, seats_available=None):
        super().__init__(available_seats)
        if seats_available is None:
            seats_available = {}
        self.seats_available = seats_available
        self.rows = rows
        self.seats_per_row = seats_per_row

    def buy_tickets(self, row_number, tickets_count):

        def is_valid(i):
            return 0 < i <= self.rows

        if not is_valid(row_number):
            return f'There is no row {row_number} in the plane!'

        seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
        if self.get_capacity(seats, tickets_count) != 'Capacity reached!':
            self.seats_available[row_number] = self.seats_per_row - tickets_count
            self.available_seats -= tickets_count
            return tickets_count
        return f'Not enough tickets on row {row_number}!'
