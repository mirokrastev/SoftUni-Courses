from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats: int, ticket_price: float, tickets_sold=0):
        super().__init__(available_seats)
        self.tickets_sold = tickets_sold
        self.ticket_price = ticket_price

    def get_total_profit(self):
        profit = self.tickets_sold * self.ticket_price
        return profit

    def get_ticket(self, tickets_count):
        if self.get_capacity(self.available_seats, tickets_count) != "Capacity reached!":
            self.available_seats -= tickets_count
            self.tickets_sold += tickets_count
        return self.get_capacity(self.available_seats, tickets_count)
