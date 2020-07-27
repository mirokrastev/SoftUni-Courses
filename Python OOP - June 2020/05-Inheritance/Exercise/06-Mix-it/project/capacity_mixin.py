class CapacityMixin:

    @staticmethod
    def get_capacity(capacity, amount):
        if amount <= capacity:
            return capacity - amount
        return 'Capacity reached!'
