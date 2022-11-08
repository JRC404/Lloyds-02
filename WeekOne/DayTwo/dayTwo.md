# Day Two

## The focus

* Conditions
* Functions / Methods
* Data Structures
* Loops

## Conditions
```python
favourite_colour = "pink"
# TODO: Create a name check if statement that will say hello to the person
# TODO: 1 if, 10 elif, 1 else
if(favourite_colour == "purple"):
    print("Nice colour choice. Purple is cool.")
    favourite_colour = "blue"

elif(favourite_colour == "red"):
    print("Red is bold. Avoid the bulls.")
    favourite_colour = "yellow"

elif(favourite_colour == "green"):
    print("Green is christmassy... It's almost Christmas. Wear it.")
    favourite_colour = "pink"

elif(favourite_colour == "orange"):
    print("The best colour. Great choice.")
    favourite_colour = "maroon"

else: # any condition that isn't the above... use the else
    print("I don't have that colour stored.")

print(favourite_colour)

# expectation?

# elif(favourite_colour = "orange"): invalid syntax
# single = means make the left equal to the right
# that isn't a condition... that's assignment

my_name = "Bob"

if(my_name == "Bob"):
    print("Ello, Bob")
elif(my_name == "Steve"):
    print("Ello.")
elif(my_name == "Ryan"):
    print("Ello.")
elif(my_name == "Dave"):
    print("Ello.")
elif(my_name == "Alan"):
    print("Ello.")
elif(my_name == "Andy"):
    print("Ello.")
elif(my_name == "Richard" or my_name == "Andy" or my_name == "Dave"):
    print("Ello.")
elif(my_name == "Susan"):
    print("Ello.")
else:
    print("Oh. Get out of my house.")
```

## Functions

* Software Developer and QE, we follow a principle:
    * DRY Principle - Don't repeat yourself
* Software Developer and QE, we follow a principle:
    * DRY Principle - Don't repeat yourself
* Software Developer and QE, we follow a principle:
    * DRY Principle - Don't repeat yourself
* Software Developer and QE, we follow a principle:
    * DRY Principle - Don't repeat yourself

* WET principle: Write everything twice
* WET principle: Write everything twice

**Lengthy but working light switch**
```python
light_on = True

# True
if(light_on == True):
    print("Well, it isn't Blackpool Illuminations. Turn the light off.")
    light_on = False
else:
    print("Dark in here, isn't it?")
    light_on = True

# False
if(light_on == True):
    print("Well, it isn't Blackpool Illuminations. Turn the light off.")
    light_on = False
else:
    print("Dark in here, isn't it?")
    light_on = True

# True
if(light_on == True):
    print("Well, it isn't Blackpool Illuminations. Turn the light off.")
    light_on = False
else:
    print("Dark in here, isn't it?")
    light_on = True

# False
if(light_on == True):
    print("Well, it isn't Blackpool Illuminations. Turn the light off.")
    light_on = False
else:
    print("Dark in here, isn't it?")
    light_on = True
```

* A function is to avoid repeated code
* A function is to allow a block of code to be called multiple times without repetition

```python
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
```

## Arrays / Lists

* Arrays / Lists are collections of items

* Lists are ordered by an index value
* The index value starts counting at 0
* If you have 5 items in your list, the index values would be like so:
    * 0, 1, 2, 3, 4

* Lists are identified by a []
```python
favourite_artists = ["Miley Cyrus", "Lady Gaga", "James Blunt"]
print(favourite_artists[0]) # first item
print(favourite_artists[1]) # second item
print(favourite_artists[2]) # third item
```