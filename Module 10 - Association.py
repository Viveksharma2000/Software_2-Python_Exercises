# Exercise 1

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Floor {target_floor} is out of range.")
            return

        print(f"Moving elevator to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


# Testing the Elevator class
if __name__ == "__main__":
    elevator = Elevator(0, 10)

    elevator.go_to_floor(5)

    elevator.go_to_floor(0)

# Exercise 2

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Floor {target_floor} is out of range.")
            return

        print(f"Moving elevator to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator {elevator_number} does not exist.")
            return

        print(f"Running elevator {elevator_number} to floor {target_floor}...")
        self.elevators[elevator_number - 1].go_to_floor(target_floor)


# Testing the Building class
if __name__ == "__main__":

    building = Building(0, 10, 3)

    building.run_elevator(1, 5)

    building.run_elevator(2, 7)

    building.run_elevator(1, 0)

# Exercise 3

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Floor {target_floor} is out of range.")
            return

        print(f"Moving elevator to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator {elevator_number} does not exist.")
            return

        print(f"Running elevator {elevator_number} to floor {target_floor}...")
        self.elevators[elevator_number - 1].go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm triggered! Moving all elevators to the bottom floor...")
        for idx, elevator in enumerate(self.elevators, 1):
            print(f"Moving elevator {idx} to the bottom floor...")
            elevator.go_to_floor(self.bottom_floor)


# Testing the Building class with fire alarm
if __name__ == "__main__":

    building = Building(0, 10, 3)

    building.run_elevator(1, 5)

    building.run_elevator(2, 7)

    building.fire_alarm()

# Exercise 4

import random


class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def drive(self):
        self.distance_travelled += self.current_speed

    def change_speed(self):
        speed_change = random.randint(-10, 15)
        self.current_speed += speed_change
        # Ensure the speed is within 0 and the max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.change_speed()
            car.drive()

    def print_status(self):
        print(f"{'Car Name':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance Travelled'}")
        print("-" * 55)
        for car in self.car_list:
            print(f"{car.name:<15}{car.max_speed:<12}{car.current_speed:<15}{car.distance_travelled}")

    def race_finished(self):
        # Check if any car has reached or exceeded the race distance
        for car in self.car_list:
            if car.distance_travelled >= self.distance:
                return True
        return False


# Main program simulating the race
if __name__ == "__main__":
    """Create a list of 10 cars statically
    cars = [
        Car("Car 1", random.randint(150, 200)),
        Car("Car 2", random.randint(150, 200)),
        Car("Car 3", random.randint(150, 200)),
        Car("Car 4", random.randint(150, 200)),
        Car("Car 5", random.randint(150, 200)),
        Car("Car 6", random.randint(150, 200)),
        Car("Car 7", random.randint(150, 200)),
        Car("Car 8", random.randint(150, 200)),
        Car("Car 9", random.randint(150, 200)),
        Car("Car 10", random.randint(150, 200))
    ]
    """
    # Create a list of 10 cars dynamically using a loop
    cars = [Car(f"Car {i + 1}", random.randint(150, 200)) for i in range(10)]
    # Create the race
    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        # Print status every 10 hours
        if hours_passed % 10 == 0:
            print(f"\n--- Hour {hours_passed} ---")
            race.print_status()

    # Final status when the race finishes
    print(f"\n--- Race Finished After {hours_passed} Hours ---")
    race.print_status()