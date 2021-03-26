class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        print(self.products[len(self.products)-1])
        print(self.products)

    def sell_product(self, id):
        self.products.pop(id)
        return self
        

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def update_price(self, percent_change, is_increased):
        percentage = percent_change / 100
        if is_increased == True:
            self.price *= (1+ percentage)
        else:
            self.price *= (1- percentage)
        return self.price

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Product: {self.price}"
    
    
    
    def print_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Product: {self.price}")


shirt = Product("shirt", "clothing", 125)
pants = Product("pants", "clothing", 550)

Nordstrom = Store("Nordstrom")
Nordstrom.add_product(shirt)
Nordstrom.add_product(pants)
# Nordstrom.sell_product(1)
Nordstrom.add_product(pants)
# shirt.print_info()

    
        