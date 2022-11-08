# inheritance.py

class Adult:
    def __init__(self, name, age, working, height, gender):
        self.name = name
        self.age = age
        self.working = working
        self.height = height
        self.gender = gender

    def work(self):
        print(f"I am going to work. My name is {self.name}.")

bob = Adult("Bob", 57, True, 185, "Male")
bob.work()

class Child(Adult):
    def __init__(self, name, age, working, height, gender, bottle):
        # super keyword allows the Child class to inherit all attributes and methods from the Adult class
        super().__init__(name, age, working, height, gender)
        self.bottle = bottle

    def use_bottle(self):
        if(self.bottle == True):
            print("Using bottle")
        else:
            print("You don't have a bottle.")

jimbob = Child("Jimbob", 16, True, 170, "Male", False) # bottle is unique to Child

jimbob.use_bottle()

# print(jimbob.bottle)
# print(bob.bottle) # AttributeError: Adult has no attribute 'bottle'

# jimbob.work()