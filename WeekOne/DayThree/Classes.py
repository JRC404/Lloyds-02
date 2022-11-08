class Employee:
    def __init__(self, id, name, role, salary, location):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary
        self.location = location

# init keyword is ran each time we create an object
# each time we create an object, it is looking for id, name, role and salary
# self refers to the instance of the class: self.id = bob.id

#! TypeError: Employee.__init__() missing 1 required positional argument: 'location'

bob = Employee(1, "Bob Bobbingson", "Tester", 18000, "Sheffield")
halle = Employee(2, "Halle Ewan", "Tester", 100000, "Fife")
print(bob.id)
print(bob.name)
print(halle.location)

class Lion:
    def __init__(self, name, age, paws, weight, mane):
        self.name = name # "Leo"
        self.age = age # 5
        self.paws = paws # 4
        self.weight = weight # "Heavyweight"
        self.mane = mane # True

    # Roar
    @staticmethod
    def roar():
        print("I am roaring.")
    # Hunt
    @staticmethod
    def hunt():
        print("I am going on a hunt.")

leo = Lion("Leo", 5, 4, "Heavyweight", True)
leo.roar() # !Lion.roar() takes 0 positional arguments but 1 was given
leo.hunt()

billy = Lion("Billy", 4, 4, "Lightweight", True)

# TODO: Create a class of your own choice: cars, humans, tv shows
# TODO: Create a function inside of the class
# TODO: Create an object like leo above

class Car:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    @staticmethod
    def honk():
        print("Honk.")

ford = Car("Henry", "Ford", 2020)
ford.honk()

class Bunny:
    def __init__(self, name, health, strength, speed, energy):
        self.name = name # Buggs
        self.health = health # 100
        self.strength = strength # 100
        self.speed = speed # 100
        self.energy = energy # 0

    # @staticmethod
    def sleep(self):
        # 20
        self.energy += 20

    def train(self):
        self.strength += 10
        self.energy -= 15

buggs = Bunny("Buggs", 100, 100, 100, 0)
print(f"Energy: {buggs.energy}")
buggs.sleep() # energy = 20
buggs.sleep() # energy = 40
buggs.sleep() # energy = 60
buggs.train() # energy = 45, strength = 110
print(f"Energy: {buggs.energy}")