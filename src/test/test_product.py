import unittest
from models.product import Food

class TestProduct(unittest.TestCase):
    def test_product_details(self):
        product = Food(1, "Milk", 1.99, "Fresh milk", "2023-12-01")
        self.assertIn("Milk", product.show_details())
