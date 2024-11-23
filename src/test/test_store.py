import unittest
from models.store import Store
from models.section import Section

class TestStore(unittest.TestCase):
    def test_add_section(self):
        store = Store(1, "Main Store", "123 Main Street")
        section = Section(1, "Food")
        store.add_section(section)
        self.assertEqual(len(store.sections), 1)
