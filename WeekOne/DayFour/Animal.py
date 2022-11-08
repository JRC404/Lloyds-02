# Animal.py

class Animal:
    def __init__(self, name, speed, energy, hunger):
        self.name = name
        self.speed = speed
        self.energy = energy
        self.hunger = hunger

    def eat(self):
        self.hunger -= 10
        self.speed -= 5
        self.energy -= 5

    def sleep(self):
        self.energy += 20
        self.hunger += 5
        self.speed += 5

    def hunt(self):
        self.hunger += 10
        self.speed -= 1
        self.energy -= 5

tommy = Animal("Tommy", 10, 10, 10)

tommy.hunt()
print(tommy.hunger)

class Dog(Animal):
    def __init__(self, name, speed, energy, hunger, working):
        super().__init__(name, speed, energy, hunger)
        self.working = working

    def bark(self):
        print(f"I am {self.name} BARK.")

lassy = Dog("Lassy", 80, 100, 0, True)

lassy.bark()

class Cat(Animal):
    def __init__(self, name, speed, energy, whiskers):
        super().__init__(name, speed, energy)
        self.whiskers = whiskers

    def roar(self):
        print(f"I am {self.name} ROAR.")

    def fur_ball(self):
        print("Cough.")

tony = Cat("Tony", 10, 100, 0, True)

tony.roar()
tony.fur_ball()

lassy.fur_ball()