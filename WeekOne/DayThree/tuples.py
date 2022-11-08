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

print(len(hogwart_houses))

# Create a tuple: FavouriteArtists
# Access an index value
# Access a range
# For loop

hogwart_list = list(hogwart_houses)
hogwart_list.append("A new house")

hogwart_houses = tuple(hogwart_list)