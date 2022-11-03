# Programming Paradigms

* Procedural
* Event-driven
* OOP

* Functional

## Object-oriented programming

* Focused on objects -> instance of a class
* Built on Classes:
    * Class: blueprint for our object


## Data Structures

* Lists = []
* Dictionary = {} -> with key:value pairs
* Tuples = ()
* Sets = {}

### Dictionaries

* Dictionaries (dict) store data inside of them
* Key : Value pair format
    * "color" : "red"
    * "name" : "Jacob"
    * "employer" : "Firebrand"
    * "age" : 57

* Dictionaries are ordered - we can refer to them by index...
    * If you are using Python 3.6 or below, dictionaries are unordered

* We cannot have duplicate keys - all of our keys are unique inside of a dictionary

* We can use the data types below inside of a dictionary:
    * int, floats, booleans, strings and lists

```python
# dictionaries.py

person_one = { 
    "name" : "Jehcub", 
    "age" : 57, 
    "employer" : "Firebrand Training LTD"
}

## Access values inside of a dictionary - Method 01

print(person_one["name"]) # Jehcub
print(person_one["age"]) # 57
print(person_one["employer"]) # Firebrand Training LTD

## Access values inside of a dictionary - Method 02

print(person_one.get("name"))
print(person_one.get("age"))
print(person_one.get("employer"))

## Saved the keys and values of the dictionary to two seperate variables

keys = person_one.keys() # all of the keys in person_one
values = person_one.values() # all of the values in person_one

print(keys)
print(values)

## Modify employer value

person_one["employer"] = "Lego Group"

print(person_one["employer"])

## Add to the dictionary

person_one["role"] = "Tea maker"

print(person_one["role"])

print("--------")

## Looping through my dictionary

for item in person_one:
    print(item) # keys

print("--------  -------")

for item in person_one:
    print(person_one[item]) # values

print("--------")
## Remove a specific item from the dictionary

person_one.pop("role")

print(person_one)

## Remove the last item in the dictionary 
# 3.6 and below... it is Russian roulette. Random choice!

person_one.popitem()

print(person_one)

## Beware of the del keyword

# del person_one # Delete person_one completely

## Clear the dictionary

person_one.clear() # this will clear the dictionary so there are no values inside but the dictionary still exists

print(person_one)

## TODO: Create a dictionary of your own:
    # Select an item
    # Add an item
    # Remove an item
    # Loop through the dictionary
```

### Tuples

* Tuples are ordered, like dictionaries and lists
* Tuples allow duplication of values
* Tuples cannot change once created

* Tuples use the () instead of the [] or {}

```python
# tuples.py

## Creating our tuple
hogwart_houses = ("Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw")

print(hogwart_houses)

## Accessing an index of our tuple

print(hogwart_houses[0]) # this is the first item in our tuple

print(hogwart_houses[-1]) # this is our last item in the tuple

## Display a range of items in our tuple

print(hogwart_houses[0:2]) # display items from index 0 to index 2, not including index 2 # ('Gryffindor', 'Slytherin')

print(hogwart_houses[1:3]) # display items from index 1 to index 3, not including index 3 # ('Slytherin', 'Hufflepuff')

for house in hogwart_houses:
    print(house)

# Create a tuple: FavouriteArtists
# Access an index value
# Access a range
# For loop

hogwart_list = list(hogwart_houses)
hogwart_list.append("A new house")

hogwart_houses = tuple(hogwart_list)
```

### Sets

* Sets use the {}
* Set is unordered, without an index
* Duplicate values are NOT allowed
* You cannot change a value of an item
* Add new items 
* Remove items

* A set can have multiple / different data types

## Try, Except

* Error Handling is important - if the application crashes, the user may move on and go somewhere else

* **try** -> try this block of code
* **except** -> if an error happens, do this
* **else** -> if there isn't an error, do this

```python
# try.py

hogwart_houses = {"Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"}

try:
    hogwart_houses.remove("Random House")
except KeyError:
    print("Looks like a Key Error")
except:
    print("An error has occured.")

try:
    print(my_age)
except NameError:
    print("The variable is not defined.")
except:
    print("Something went wrong.")

print("Hello World")
```