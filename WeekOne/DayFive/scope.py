# Global scope

my_name = "Jacob" # global variable
my_age = 10 # global variable

print(f"Global my_age is equal to {my_age}")
# print(my_name) 

def local_function():
    global my_age
    # my_age = 57 # created a local variable called my_age, different to the global one
    my_age += 1
    print(f"Local my_age is equal to {my_age}")

local_function()

def print_name():
    # global my_name # use the global variable my_name
    # do not create a new one in here
    my_name = "Bob"
    my_name = "Mr. " + my_name
    print(f"My name is {my_name}.")

print_name()

# Local scope


print(my_name)
print(my_age)