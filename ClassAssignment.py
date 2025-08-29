# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.__storage = storage   # Private attribute to demonstrate encapsulation
        self.__battery = battery   # Private attribute

    # Method to display phone info
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        print(f"Storage: {self.__storage}GB, Battery: {self.__battery}mAh")

    # Method to charge battery
    def charge(self, amount):
        self.__battery += amount
        print(f"{self.model} charged by {amount}mAh. Current battery: {self.__battery}mAh")

    # Getter for battery
    def get_battery(self):
        return self.__battery

    # Setter for storage (example of encapsulation)
    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Invalid storage value")


# Inheritance example: GamingPhone inherits from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Overriding show_info method (polymorphism)
    def show_info(self):
        super().show_info()
        print(f"Cooling System: {self.cooling_system}")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 4000)
phone2 = GamingPhone("Asus", "ROG Phone 7", 256, 6000, "Advanced Cooling")

# Test methods
phone1.show_info()
print()
phone2.show_info()
phone2.charge(500)
phone2.set_storage(512)
print()
phone2.show_info()
