from models.product import Food, Technology, Clothing
from models.section import Section
from models.store import Store

class Menu:
    def __init__(self):
        self.store = Store(1, "Main Store", "123 Main Street")

    def start(self):
        while True:
            print("\n--- Warehouse Management System ---")
            print("1. Add Section")
            print("2. Add Product to Section")
            print("3. List Sections")
            print("4. List Products in a Section")
            print("5. Search Product by Name")
            print("6. Remove Product from Section")
            print("7. Exit")
            
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_section()
            elif choice == "2":
                self.add_product_to_section()
            elif choice == "3":
                self.list_sections()
            elif choice == "4":
                self.list_products_in_section()
            elif choice == "5":
                self.search_product_by_name()
            elif choice == "6":
                self.remove_product_from_section()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def add_section(self):
        section_id = input("Enter Section ID: ")
        section_name = input("Enter Section Name: ")
        self.store.add_section(Section(section_id, section_name))
        print(f"Section '{section_name}' added successfully.")

    def add_product_to_section(self):
        if not self.store.sections:
            print("No sections available. Please add a section first.")
            return

        print("\nAvailable Sections:")
        for section in self.store.sections:
            print(f"{section.section_id}: {section.name}")
        
        section_id = input("Enter Section ID to add a product: ")
        section = self.store.find_section_by_id(section_id)

        if section:
            product_type = input("Enter Product Type (Food, Technology, Clothing): ").strip().lower()
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            description = input("Enter Product Description: ")

            if product_type == "food":
                expiration_date = input("Enter Expiration Date (YYYY-MM-DD): ")
                product = Food(product_id, name, price, description, expiration_date)
            elif product_type == "technology":
                warranty = int(input("Enter Warranty (in years): "))
                product = Technology(product_id, name, price, description, warranty)
            elif product_type == "clothing":
                size = input("Enter Size: ")
                product = Clothing(product_id, name, price, description, size)
            else:
                print("Invalid product type.")
                return
            
            section.add_product(product)
            print(f"Product '{name}' added to Section '{section.name}'.")
        else:
            print("Section not found.")

    def list_sections(self):
        if not self.store.sections:
            print("No sections available.")
        else:
            print("\nSections in the Store:")
            for sec in self.store.list_sections():
                print(sec)

    def list_products_in_section(self):
        if not self.store.sections:
            print("No sections available.")
            return

        section_id = input("Enter Section ID: ")
        section = self.store.find_section_by_id(section_id)

        if section:
            print(f"\nProducts in Section '{section.name}':")
            for product_details in section.list_products():
                print(product_details)
        else:
            print("Section not found.")

    def search_product_by_name(self):
        if not self.store.sections:
            print("No sections available.")
            return

        product_name = input("Enter Product Name to Search: ")

        found = False
        for section in self.store.sections:
            product = section.find_product_by_name(product_name)
            if product:
                print(f"\nProduct found in Section '{section.name}':")
                print(product.show_details())
                found = True
                break
        
        if not found:
            print("Product not found.")

    def remove_product_from_section(self):
        if not self.store.sections:
            print("No sections available.")
            return

        section_id = input("Enter Section ID to Remove a Product: ")
        section = self.store.find_section_by_id(section_id)

        if section:
            product_id = input("Enter Product ID to Remove: ")
            section.remove_product(product_id)
            print(f"Product with ID '{product_id}' removed from Section '{section.name}'.")
        else:
            print("Section not found.")
