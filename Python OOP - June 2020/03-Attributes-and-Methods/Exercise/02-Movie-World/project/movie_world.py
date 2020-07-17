class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers
                    if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds
               if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'

        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        if dvd.is_rented:
            return f'DVD is already rented'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers
                    if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds
               if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        result = "".join(f'{customer}\n' for customer in self.customers)
        result += "\n".join(f'{movie}' for movie in self.dvds)

        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10