# classes.py

## Classes should use Pascal casing: Student, StudentClass
## In any programming language, this is the standard

class Student:
    def __init__(self, student_id, full_name, role, enrolled):
        self.student_id = student_id
        self.full_name = full_name
        self.role = role
        self.enrolled = enrolled

    def enrol(self):
        self.enrolled = True

    def expelled(self):
        self.enrolled = False

    def print_details(self):
        print(f"Hi, I am {self.full_name}. My Student ID is {self.student_id}. My role at my company is {self.role}.")

# function is a block of code that we can reuse to avoid rewriting code
# in a class or object, a function is called a method
# alt + z will wrap text

bob = Student(1, "Bob Bobbington", "Engineer", False) # object
sally = Student(2, "Sally Bobbington", "Engineer", False) # object

print(bob.enrolled) # false
bob.enrol()
print(bob.enrolled) # true

print("--------")

print(sally.enrolled) # false
sally.enrol() # calling the enrol method... without the () it doesn't do anything
print(sally.enrolled) # true

bob.expelled()
sally.expelled()

print("--------")
print(bob.enrolled)
print(sally.enrolled)

bob.print_details()

# bobby = {
#     "name" : "Bob Bobbington",
#     "student_id" : 1,
#     "role" : "Engineer",
#     "enrolled" : False
# }


# sally = {
#     "name" : "Sally Bobbington",
#     "student_id" : 2,
#     "role" : "Engineer",
#     "enrolled" : False
# }