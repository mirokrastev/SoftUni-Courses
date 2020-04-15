class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [i for i in self.products if i[0] == first_letter]

    def __repr__(self):
        res =  f'Items in the {self.name} catalogue:\n'
        self.products.sort()
        res += '\n'.join(self.products)
        return res