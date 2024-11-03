# Exercise 1

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

# Main program
if __name__ == "__main__":
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    print("Publication Information:\n")
    magazine.print_information()
    print("\n")
    book.print_information()

# Exercise 2

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def drive(self):
        self.distance_travelled += self.current_speed

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kilowatt-hours (kWh)

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters (l)

# Main program
if __name__ == "__main__":
    # Creating one electric car and one gasoline car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Setting speeds for both cars
    electric_car.current_speed = 100
    gasoline_car.current_speed = 120

    # for 3 hours drive
    for _ in range(3):
        electric_car.drive()
        gasoline_car.drive()

    print(f"Electric Car ({electric_car.registration_number}) travelled: {electric_car.distance_travelled} km")
    print(f"Gasoline Car ({gasoline_car.registration_number}) travelled: {gasoline_car.distance_travelled} km")