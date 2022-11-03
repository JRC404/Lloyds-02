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

print("-------- HELLO -------")

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