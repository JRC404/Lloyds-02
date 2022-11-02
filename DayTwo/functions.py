# light_on = True

# def is the keyword for our function - 33 lines for 4 switches

def light_switch(light_on):
    if(light_on == True):
        print("Well, it isn't Blackpool Illuminations. Turn the light off.")
        light_on = False
    else:
        print("Dark in here, isn't it?")
        light_on = True
    

# light_switch(True) # Blackpool
# light_switch(True) # Blackpool
# light_switch(False) # Dark
# light_switch(False) # Dark

# def is the keyword to create a function
# without def, the code doesn't know what it is doing
def honk_horn():
    print("Honk.")
    print("Swear.")

honk_horn()
honk_horn()
honk_horn()
honk_horn()
honk_horn()

def get_dressed():
    print("Put socks on")
    print("Put shoes on")
    print("Put pants / trouser on")

get_dressed()
get_dressed()
get_dressed()

def addition(number_one, number_two):
    print(number_one + number_two)

def subtraction(number_one, number_two): # -
    print(number_one - number_two)

def multiplication(number_one, number_two): # *
    print(number_one * number_two)

def division(number_one, number_two): # /
    print(number_one / number_two)

addition(10, 20) # what will be printed to the console?
subtraction(100, 30)
multiplication(50, 10)
division(9, 3)

# create a function that prints the username to a string
def print_name(username):
    print(f"Hello, your name is {username}")
    print("Hello, your name is " + username)

# create a function that prints the age to a string
def print_age(age):
    print(f"Hello, your age is {age}")

def example():
    print("Ummmm")

def print_information(name, age):
    print(f"Your name is {name} and you are {age} years old.")

print_information("Jehcub", 57)

# String interpolation -> put a variable inside of a string

print_name("Owais")
print_age(62)

example()