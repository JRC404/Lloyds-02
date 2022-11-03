# sets.py

hogwart_houses = {"Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"}

print(hogwart_houses)

print(len(hogwart_houses)) # this can used on all data structures

for house in hogwart_houses:
    print(house)

print("Slytherin" in hogwart_houses) # True
print("slytherin" in hogwart_houses) # False

hogwart_houses.add("Random House")
hogwart_houses.add("Random House")
hogwart_houses.add("Random House")
hogwart_houses.add("Random House")
hogwart_houses.add("Random House")

print("--------")
for house in hogwart_houses:
    print(house)
print("--------")

# you can have different data types like below
# doesn't make sense out of context, try to use a dictionary instead

random_set = ("cheese", 5, True, "hello")

drawer = {
    "favourite_food" : "cheese",
    "favourite_number" : 5,
    "light_on" : True,
    "favourite_greeting" : "hello"
}

hogwart_houses.update(drawer.values())

for item in hogwart_houses:
    print(item)

hogwart_houses.remove("Random House")
hogwart_houses.remove("Random House")

print("---------")

for item in hogwart_houses:
    print(item)

print("Hello, World.")