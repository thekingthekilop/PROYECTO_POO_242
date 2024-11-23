import unittest
from models.section import Section
from models.product import Food

class TestSection(unittest.TestCase):
    def test_add_product(self):
        section = Section(1, "Food")
        product = Food(1, "Milk", 1.99, "Fresh milk", "2023-12-01")
        section.add_product(product)
        self.assertEqual(len(section.products), 1)
