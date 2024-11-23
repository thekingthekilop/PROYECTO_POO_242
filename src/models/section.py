class Section:
    def __init__(self, section_id, name):
        self.section_id = section_id
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [prod for prod in self.products if prod.product_id != product_id]

    def find_product_by_name(self, name):
        return next((prod for prod in self.products if prod.name == name), None)

    def find_product_by_id(self, product_id):
        return next((prod for prod in self.products if prod.product_id == product_id), None)

    def list_products(self):
        return [prod.show_details() for prod in self.products]

    def sort_products_by_expiration(self):
        self.products.sort(key=lambda p: getattr(p, "expiration_date", None))
