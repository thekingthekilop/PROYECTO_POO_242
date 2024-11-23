class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def show_details(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Description: {self.description}"

class Food(Product):
    def __init__(self, product_id, name, price, description, expiration_date):
        super().__init__(product_id, name, price, description)
        self.expiration_date = expiration_date

    def show_details(self):
        return super().show_details() + f", Expiration Date: {self.expiration_date}"

class Technology(Product):
    def __init__(self, product_id, name, price, description, warranty):
        super().__init__(product_id, name, price, description)
        self.warranty = warranty

    def show_details(self):
        return super().show_details() + f", Warranty: {self.warranty} years"

class Clothing(Product):
    def __init__(self, product_id, name, price, description, size):
        super().__init__(product_id, name, price, description)
        self.size = size

    def show_details(self):
        return super().show_details() + f", Size: {self.size}"
        